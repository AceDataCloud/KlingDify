# Kling capability mapping

Compared with [MCPs at f0eed10abf31](https://github.com/AceDataCloud/MCPs/tree/f0eed10abf310824cb4c33d4944c63d3654ac95b/kling) and the public API contract at PlatformBackend `fa94598267a82545fb1afed6ee26bafd6cbb9ca7`.

The table maps service operations to Dify tools. Different MCP helper functions may use the same action selector or structured JSON input.

| MCP function | Dify equivalent | Notes |
|---|---|---|
| `kling_generate_with_assets` | `kling_generate_video` |  |
| `kling_list_models` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `kling_list_actions` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `kling_generate_turbo_video` | `kling_generate_video` |  |
| `kling_generate_storyboard` | `kling_generate_video` |  |
| `kling_goods_studio` | `kling_goods_studio` |  |
| `kling_video_commerce` | `kling_video_commerce` |  |
| `kling_get_task` | `kling_task_retrieve` | Set action=retrieve |
| `kling_get_tasks_batch` | `kling_tasks_retrieve_batch` | Set action=retrieve_batch |
| `kling_lip_sync` | `kling_lip_sync` |  |
| `kling_talking_photo` | `kling_talking_photo` |  |
| `kling_generate_motion` | `kling_generate_motion` |  |
| `kling_generate_video` | `kling_generate_video` | Set action=text2video |
| `kling_generate_video_from_image` | `kling_generate_video` | Set action=image2video |
| `kling_extend_video` | `kling_generate_video` | Set action=extend |

## Parameter equivalents

- `kling_generate_with_assets`: `request` → Expanded request fields (including nested JSON inputs).
- `kling_generate_turbo_video`: `request` → Expanded request fields (including nested JSON inputs).
- `kling_generate_storyboard`: `request` → Expanded request fields (including nested JSON inputs).
- `kling_goods_studio`: `request` → Expanded request fields (including nested JSON inputs).
- `kling_video_commerce`: `request` → Expanded request fields (including nested JSON inputs).
- `kling_get_tasks_batch`: `task_ids` → ids.

## Verification boundary

Contract examples and regression tests cover request validation, transport and task handling. Actual Dify browser cases are recorded separately in `tests/e2e-results.json` and `tests/e2e-audit.json` when available. A schema test is not a successful paid generation. Unsupported service availability and untested advanced combinations must not be described as passed.
