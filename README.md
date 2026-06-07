# ZAgent - AI Agent with Stealth Browser & Chat UI

> Public release repository for [ctz168/zagent](https://github.com/ctz168/zagent)

## Features

- **AI Chat Interface** - Web-based chat UI with SSE streaming, markdown rendering, and tool call visualization
- **Stealth Browser** - Anti-detection browser automation using chromedp (Go native implementation)
  - 15 browser tools: start, navigate, click, fill, type, press-key, screenshot, eval, content, cookies, scroll, wait, close, status, test
  - 12 stealth patches: webdriver removal, plugins mock, languages mock, chrome.runtime masking, Permissions API override, and more
- **Workflow Engine** - GitHub Actions-style multi-step automation
- **Memory System** - Persistent memory with search, recall, and summarization
- **Alarm System** - One-time, daily, weekly, monthly, and custom interval alarms
- **TTS Support** - Browser-based and IndexTTS server text-to-speech
- **File Management** - Read, write, and manage files with line-by-line code retrieval
- **AICQ Integration** - Real-time messaging via AICQ WebSocket protocol

## Quick Start

1. Download the latest release from [Releases](https://github.com/ctz168/zagent_r/releases)
2. Extract the archive for your platform
3. Configure your LLM API settings: `./zagent llm configure`
4. Start the agent: `./zagent -name MyAgent`
5. Open the web UI at `http://localhost:8181`

## Supported Platforms

| Platform | Architecture | File |
|----------|-------------|------|
| Linux | amd64 | `zagent-linux-amd64.tar.gz` |
| Linux | arm64 | `zagent-linux-arm64.tar.gz` |
| macOS | amd64 | `zagent-darwin-amd64.tar.gz` |
| macOS | arm64 | `zagent-darwin-arm64.tar.gz` |
| Windows | amd64 | `zagent-windows-amd64.zip` |
| Windows | arm64 | `zagent-windows-arm64.zip` |

## Requirements

- **Chrome/Chromium** (required for stealth browser features)
- **LLM API** (OpenAI-compatible, Anthropic, or Ollama)

## Release Sync

This repository automatically syncs releases from the private [ctz168/zagent](https://github.com/ctz168/zagent) repository. When a new release is published there, it is automatically mirrored here.

## License

See the source repository for license information.
