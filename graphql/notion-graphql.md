# Notion GraphQL

## Overview

**Provider:** Notion  
**Native GraphQL:** No  
**Schema type:** Conceptual data model derived from the Notion REST API  
**REST API docs:** https://developers.notion.com/reference/intro  
**REST base URL:** https://api.notion.com  

## Description

Notion does not expose a public GraphQL endpoint. Notion's public API is a versioned REST API (`api.notion.com/v1`). The GraphQL schema in `notion-schema.graphql` is a comprehensive conceptual model derived from Notion's REST API object types, suitable for tooling, catalog enrichment, code generation, and integration mapping.

## Core Object Types

The schema covers all major Notion API object types:

- **Database** — A structured collection of pages with typed property schemas
- **Page** — A document or record inside a database or workspace
- **Block** — The fundamental content unit; includes 25+ subtypes (paragraph, heading1-3, bulleted_list_item, numbered_list_item, to_do, toggle, child_page, child_database, embed, image, video, file, pdf, code, callout, quote, equation, divider, table_of_contents, column, column_list, link_preview, synced_block, template, link_to_page, table, table_row, bookmark, unsupported)
- **User / Person / Bot** — Workspace members and integration bots
- **Comment** — Threaded discussion items attached to pages or blocks
- **Property** — Typed schema fields on databases; includes 19+ subtypes (title, rich_text, number, select, multi_select, date, people, files, checkbox, url, email, phone_number, formula, relation, rollup, created_time, created_by, last_edited_time, last_edited_by, status, unique_id, verification)
- **RichText** — Inline formatted text segments with annotations
- **File / ExternalFile** — Hosted or externally linked file references
- **FileUpload** — Managed multi-part file upload objects
- **DataSource** — External data source integrations
- **Emoji / Icon / Cover** — Visual adornments on pages and databases
- **Parent** — Union of workspace, page, database, and block parent references
- **Annotation** — Inline text styling (bold, italic, strikethrough, underline, code, color)

## References

- REST API reference: https://developers.notion.com/reference/intro
- Block object: https://developers.notion.com/reference/block
- Page object: https://developers.notion.com/reference/page
- Database object: https://developers.notion.com/reference/database
- User object: https://developers.notion.com/reference/user
- Comment object: https://developers.notion.com/reference/comment-object
- Rich text object: https://developers.notion.com/reference/rich-text
- File object: https://developers.notion.com/reference/file-object
- Property object: https://developers.notion.com/reference/property-object
- Page property values: https://developers.notion.com/reference/page-property-values
- Data source object: https://developers.notion.com/reference/data-source
- File upload object: https://developers.notion.com/reference/file-upload
- JavaScript SDK: https://github.com/makenotion/notion-sdk-js
