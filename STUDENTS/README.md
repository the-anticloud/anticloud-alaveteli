# Students — ALAVETELI

**Project:** ALAVETELI  
**Category:** GOVERNMENT  
**Upstream:** https://github.com/mysociety/alaveteli  
**Pinned commit:** `6ad79e9334c4131078c6a67560452bfd5e7781b8`  
**Assurance:** 16/16 checks passing  
**Ledger head:** `f2daaf2a0f1103b1b92be7c0b85cb07ec7cca312093eaa1d7392785bb22e5874`  
**Date:** October 2026

## What this project gives you

A complete worked example of offline-first packaging with a cryptographic audit
chain: source pinned at `6ad79e9334c4131078c6a67560452bfd5e7781b8`, a 16-check assurance suite, an evidence register
with per-check hashes, and an AIOSS ledger chain ending at `f2daaf2a0f1103b1b92be7c0b85cb07ec7cca312093eaa1d7392785bb22e5874`.

## Learn by verifying

```
python tools/run_bench.py --out BENCH.json
```

Then take any row from `ISOLATED_LAB_RESULTS/03_Result_Register.md`, recompute
the SHA3-256 of its evidence file, and confirm it matches. If it does not match,
the record has been altered — that is the whole point of the chain.

## Licence

Apache 2.0 terms apply to study and teaching use.
