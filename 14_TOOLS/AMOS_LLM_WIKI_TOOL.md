---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: Amos Llm Wiki Tool
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# AMOS LLM Wiki — Tools

The LLM Wiki subsystem is supported by a small set of tools that make ingest, query, and lint easier.

## 1. Tool Overview

The LLM Wiki tools provide a complete pipeline for knowledge ingestion, retrieval, and maintenance within the AMOS vault structure.

| Tool | Function | Category | Authority Required |
| :--- | :--- | :--- | :--- |
| Obsidian Web Clipper | Browser-to-markdown conversion | Ingestion | network:read |
| Local Attachment Download | Asset management for clipped content | Ingestion | file:write |
| qmd | Hybrid BM25/vector search | Retrieval | file:read |
| grep / tail | Log file inspection | Inspection | file:read |
| Dataview | Dynamic table rendering | Presentation | file:read |

## 2. Obsidian Web Clipper

Browser extension that converts web articles to markdown. Save clips to `11_KNOWLEDGE/LLM_WIKI/raw/`.

### 2.1 Configuration

```yaml
web_clipper_config:
  target_directory: "11_KNOWLEDGE/LLM_WIKI/raw/"
  frontmatter_template:
    - "title: {{page_title}}"
    - "source_url: {{page_url}}"
    - "clip_date: {{current_date}}"
    - "clip_method: web_clipper"
    - "tags: [llm-wiki, clipped]"
  asset_handling:
    download_images: true
    asset_path: "11_KNOWLEDGE/LLM_WIKI/raw/assets/"
    max_image_size_mb: 10
  content_processing:
    strip_ads: true
    preserve_code_blocks: true
    preserve_tables: true
    max_content_length: 50000
```

### 2.2 Invocation Protocol

```yaml
clip_invocation:
  trigger: "User activates Web Clipper on target page"
  steps:
    - "Extract page content (title, body, metadata)"
    - "Convert HTML to markdown preserving structure"
    - "Download and reference local assets"
    - "Generate frontmatter from template"
    - "Write to target directory"
    - "Log clip in LLM_WIKI_LOG"
    - "Return clip receipt with file path"
  output_class: "OBSERVATION"
  authority_check: "file:write:11_KNOWLEDGE/LLM_WIKI/raw/"
```

### 2.3 Quality Checks

| Check | Condition | Action on Failure |
| :--- | :--- | :--- |
| Content length | >100 characters | Reject (too short) |
| Duplicate detection | Similar content exists | Warn; allow override |
| Source accessibility | URL reachable | Retry; fail if persistent |
| Asset download | All images downloaded | Warn; continue with partial assets |

## 3. Local Attachment Download

In Obsidian → Settings → Files and links, set "Attachment folder path" to `11_KNOWLEDGE/LLM_WIKI/raw/assets/`. After clipping, use the "Download attachments for current file" command.

### 3.1 Attachment Management

```yaml
attachment_management:
  storage_path: "11_KNOWLEDGE/LLM_WIKI/raw/assets/"
  naming_convention: "descriptive_filename_with_context"
  organization:
    method: "flat_directory"
    max_files_per_directory: 1000
  deduplication:
    method: "content_hash"
    hash_algorithm: "sha256"
    action_on_duplicate: "reference_existing"
  cleanup:
    orphan_check_frequency: "weekly"
    action: "flag_orphans_for_review"
```

### 3.2 Download Protocol

```yaml
attachment_download:
  trigger: "User invokes 'Download attachments for current file'"
  steps:
    - "Parse current markdown file for image/asset references"
    - "Identify missing local attachments"
    - "Download missing assets from source URLs"
    - "Store in attachment folder"
    - "Update markdown references to local paths"
    - "Log download in attachment manifest"
    - "Return download receipt"
  authority_check: "file:write:11_KNOWLEDGE/LLM_WIKI/raw/assets/"
```

## 4. qmd (Optional)

When the wiki grows past a few hundred pages, install `qmd` for hybrid BM25/vector search over markdown. Use only the official repository the user provides; do not guess a URL.

### 4.1 Hybrid Search Architecture

```yaml
qmd_search:
  index_type: "hybrid_BM25_vector"
  bm25_component:
    tokenizer: "unicode_word"
    k1: 1.5
    b: 0.75
  vector_component:
    embedding_model: "local_sentence_transformer"
    dimension: 384
    similarity: "cosine"
  fusion_method: "reciprocal_rank_fusion"
  fusion_parameters:
    k: 60  # RRF constant
  query_expansion:
    enabled: true
    max_expansion_terms: 5
```

### 4.2 Query Protocol

```yaml
wiki_query:
  input: "Natural language query string"
  steps:
    - "Tokenize query for BM25 component"
    - "Embed query for vector component"
    - "Execute BM25 search over indexed pages"
    - "Execute vector similarity search"
    - "Fuse results using reciprocal rank fusion"
    - "Rank by combined score"
    - "Return top-K results with excerpts"
  output_format:
    - "page_title: string"
    - "file_path: string"
    - "relevance_score: float"
    - "excerpt: string"
    - "match_source: enum[bm25, vector, both]"
  output_class: "OBSERVATION"
```

### 4.3 Index Management

```yaml
index_management:
  build_trigger:
    - "Initial wiki load"
    - "New page added"
    - "Page significantly modified"
    - "Manual rebuild requested"
  incremental_update:
    method: "diff_based"
    detect_changes: "file_hash_comparison"
    update_scope: "changed_pages_only"
  full_rebuild:
    trigger: "Index corruption or major restructuring"
    method: "full_reindex"
    estimated_time: "proportional_to_page_count"
```

## 5. grep / tail

At small scale the `LLM_WIKI_LOG` is grep-parseable:

```sh
grep "^## \[" 11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md | tail -5
```

### 5.1 Log Format

```yaml
wiki_log_entry:
  format: "## [YYYY-MM-DD HH:MM:SS] EVENT_TYPE: description"
  event_types:
    - "CLIP: New page clipped from web"
    - "INGEST: Page processed and indexed"
    - "QUERY: Search query executed"
    - "MODIFY: Existing page modified"
    - "DELETE: Page removed"
    - "ERROR: Operation failed"
  example: "## [2026-09-04 10:30:00] CLIP: Clipped 'EEG Foundation Models' from arxiv.org"
```

### 5.2 Common Inspection Commands

```bash
# Last 5 clips
grep "^## \[.*\] CLIP:" 11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md | tail -5

# Errors in last 24 hours
grep "^## \[2026-09-04.*\] ERROR:" 11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md

# All pages modified
grep "^## \[.*\] MODIFY:" 11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md
```

## 6. Dataview

If YAML frontmatter is added to wiki pages, Dataview can render dynamic tables of sources, concepts, and entities.

### 6.1 Frontmatter Schema

```yaml
required_fields:
  - "title: string"
  - "source_url: string (optional)"
  - "clip_date: date"
  - "tags: list[string]"
optional_fields:
  - "authors: list[string]"
  - "publication_date: date"
  - "domain: string"
  - "confidence: float"
  - "epistemic_class: enum[OBSERVATION, SOURCE_CLAIM, DERIVED]"
```

### 6.2 Example Dataview Queries

```dataview
TABLE source_url, clip_date, confidence
FROM "11_KNOWLEDGE/LLM_WIKI/wiki"
WHERE contains(tags, "llm-wiki")
SORT clip_date DESC
LIMIT 20
```

```dataview
TABLE authors, publication_date, domain
FROM "11_KNOWLEDGE/LLM_WIKI/wiki"
WHERE contains(tags, "neural-networks")
SORT publication_date DESC
```

## 7. Cross-Vault References

- [[00_ROOT/AMOS_LLM_WIKI|AMOS_LLM_WIKI]]
- [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC|LLM_WIKI_MOC]]
- [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]] — Tools plane governing this tool
- [[09_PROTOCOLS/AGENT_TOOL_INTERACTION_PROTOCOL|AGENT_TOOL_INTERACTION_PROTOCOL]] — Tool invocation protocol
- [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE_MOC]] — Knowledge plane ingested by these tools

______________________________________________________________________

**MOC:** [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]]
