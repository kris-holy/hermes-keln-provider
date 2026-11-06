# Keln provider for Hermes

Use [Keln](https://keln.ai) models in [Hermes Agent](https://github.com/NousResearch/hermes-agent)
as a first-class provider: pick **Keln** in `hermes model`, or run `hermes chat --provider keln`.

Keln is an inference platform for open models with an OpenAI-compatible API. Keln maintains this
plugin. It is not affiliated with NousResearch.

## Why a plugin?

Keln's API is OpenAI-compatible, so Hermes can reach it through a hand-written custom provider. The
plugin adds:

| | Custom provider | This plugin |
|---|---|---|
| Choosing Keln | A manual `config.yaml` block | `--provider keln`, or a row in `hermes model` |
| Model picker | The list you type or the raw catalog | The live catalog, with a tool-calling list as the fallback |
| Auxiliary tasks | The main model | `zai-org/glm-5.3-flash`, a lower-cost model |

## Install

```sh
hermes plugins install keln-provider
```

## Configure

1. Sign up at [app.keln.ai](https://app.keln.ai/signup). Open **Keys** → **Create key** and copy
   the key.
2. Save the key in Hermes:

   ```sh
   hermes config set KELN_API_KEY <your-key>
   ```

3. Pick **Keln** in `hermes model`, or run `hermes chat --provider keln`.

## Models

Hermes reads the live catalog from `https://api.keln.ai/v1/models`, which also publishes each
model's context window and input types. If that request fails, the picker shows this list of models
with tool calling:

| Model | Input |
|---|---|
| `moonshotai/kimi-k3` | text, images |
| `qwen/qwen3.8-2.4t-a95b` | text |
| `zai-org/glm-5.3` | text |
| `zai-org/glm-5.3-flash` | text, images |
| `deepseek-ai/deepseek-v4.1-flash` | text, images |

The live catalog also lists `cloudflare/clef` and `typesafe/jev-1.14`. These are decision models.
They answer typed questions through `/v1/decisions` and do not write text, so they do not work as
the agent's main model.

Prices are on [Models & pricing](https://docs.keln.ai/models-pricing/).

## Security and footprint

- **Network:** Hermes sends your requests, including prompts and any files or images in them, to
  `https://api.keln.ai` using your `KELN_API_KEY`. See
  [Privacy & zero data retention](https://docs.keln.ai/capabilities/privacy/).
- **Code:** the plugin registers 1 provider profile. It adds no tools, hooks or middleware, runs no
  shell commands or background processes, reads no files, and has no Python dependencies.
- **Credentials:** Hermes holds the key. The plugin only declares the variable name.
- **Telemetry:** the plugin sends no telemetry.

## Compatibility

Requires Hermes `>=0.22.6`.

## Changelog

- **1.0.0:** first release.

## License

MIT
