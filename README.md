# faida-mcp
<!-- mcp-name: io.github.gabrielmahia/faida-mcp -->

[![faida-mcp Glama score](https://glama.ai/mcp/servers/gabrielmahia/faida-mcp/badges/score.svg)](https://glama.ai/mcp/servers/gabrielmahia/faida-mcp)
[![smithery badge](https://smithery.ai/badge/@gabrielmahia/faida-mcp)](https://smithery.ai/server/@gabrielmahia/faida-mcp)


---
**Compatible with `claude-sonnet-5`** (released 2026-06-30) — Anthropic's most agentic
Sonnet yet. Runs multi-step tool chains end-to-end without stopping short.
Install: `pip install faida-mcp` · Use with any MCP client.

---


> Kenya capital markets via MCP — Treasury bonds, NSE equities, unit trusts, diaspora investment

[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue)](https://github.com/gabrielmahia/faida-mcp)
[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/gabrielmahia/faida-mcp)
[![Layer](https://img.shields.io/badge/Layer-Economic-orange)](https://github.com/gabrielmahia/faida-mcp)

## Install

```bash
pip install faida-mcp
```

## What it does

6 MCP tools covering Kenya investment and capital markets. 1st world equivalent: **Fidelity / Schwab**.

| Tool | Description |
|------|-------------|
| `treasury_bond_calculator` | Yield, total return, tax calculation for CBK bonds |
| `nse_equities_guide` | NSE first-time investor guide — CDS, costs, brokers |
| `unit_trust_comparison` | Risk/return comparison: MMF, bond, equity funds |
| `diaspora_investment_guide` | M-Akiba, REITs, NSE access for overseas investors |
| `nse_ipo_guide` | How to participate in Kenya IPOs |
| `financial_literacy_kenya` | 50/30/20 rule, compound interest, SACCO vs bank |

## Usage

```bash
# Run as standalone MCP server
faida-mcp

# Or add to Claude Desktop / any MCP client
# Add to your MCP config: {"command": "faida-mcp"}
```

## Part of the Kenya Coordination Infrastructure Stack

This is one of 23 MCP servers covering the full coordination infrastructure of East Africa:

**Economic:** mpesa · mkopo · bima · soko · sifa · remit · kra · faida  
**Physical:** wapimaji · nishati · usafiri · ardhi  
**Social:** afya · afya-ya-akili · elimu · kazi · haki-ya-kazi · kilimo · jumuia  
**Civic:** nyumba · habari · mazingira · civic-agent-kit  

→ [The Nairobi Stack](https://gabrielmahia.github.io/nairobi-stack)  
→ [Full Portfolio](https://gabrielmahia.github.io)

## Trust Integrity

All data in this server is **clearly labeled DEMO** where synthetic. Verify all operational data with the relevant Kenyan government authority before use.

## License

MIT © Gabriel Mahia | [AI-KungFU](https://github.com/gabrielmahia) | contact@aikungfu.dev

> *Decision infrastructure for East Africa*

## Part of the East Africa Coordination Stack

This MCP server is one of 32 tools in the Kenya coordination infrastructure.
Connect it to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) —
the coordination event bus that routes signals between domains automatically.

```bash
pip install africa-coord-bus
```

All 32 servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)
Live demo: [coord-cascade-demo](https://github.com/gabrielmahia/coord-cascade-demo)

## IP & Collaboration

MIT licensed. Feedback via GitHub Issues only — pull requests are not accepted. Demo data is labeled DEMO and is not suitable for operational decisions. Full policy: [docs/architecture/IP_POLICY.md](docs/architecture/IP_POLICY.md). Security reports: see [SECURITY.md](SECURITY.md).
