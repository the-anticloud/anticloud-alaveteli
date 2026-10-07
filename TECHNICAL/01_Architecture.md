# Technical Architecture — ALAVETELI

**Upstream:** [https://github.com/mysociety/alaveteli](https://github.com/mysociety/alaveteli)
**License:** MIT
**Category:** GOVERNMENT
**Anticloud Integration:** PAX L5 Narrow L2 General 27B + AIOSS + Offline-First

## Upstream Description

Freedom of information request platform

## Anticloud Architectural Changes

1. PAX L5 Narrow L2 General 27B local document processing — air-gapped sovereign deployment
2. AIOSS tamper-evident audit trail for all citizen record modifications
3. AES-256 encryption aligned with FIPS 140-2 for all stored data
4. Single-binary deployment on sovereign government infrastructure
5. Zero third-party cloud: no data leaves government-controlled servers
6. Role-based access control with cryptographic audit log of all access
7. Offline NLP pipeline for form processing and classification
8. Open-source supply chain: all dependencies pinned, audited, MIT/Apache 2.0

## Integration Points

- **PAX Inference Socket:** Local HTTP endpoint at `127.0.0.1:11434/v1/chat` — same OpenAI-compatible API, zero cloud
- **AIOSS Hook:** Every write operation calls `aioss_append(event, payload)` before commit
- **Encryption Layer:** All file I/O routed through `anticloud_crypto.encrypt_at_rest()`
- **Single Binary Build:** `pyinstaller anticloud_alaveteli.spec` or `go build -o alaveteli`

## Deployment Modes

| Mode | Hardware | Notes |
| --- | --- | --- |
| Edge CPU | Raspberry Pi 4 / Intel NUC | Full feature set, PAX on CPU |
| Desktop GPU | RTX 3060 / A10 | PAX GPU inference, <1s latency |
| Server | 2× A100 | Full batch throughput |
| Air-gapped | Any x86/ARM | Zero network dependency |