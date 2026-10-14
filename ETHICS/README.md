# Ethics — ALAVETELI

**Project:** ALAVETELI  
**Category:** GOVERNMENT  
**Upstream:** https://github.com/mysociety/alaveteli  
**Pinned commit:** `6ad79e9334c4131078c6a67560452bfd5e7781b8`  
**Assurance:** 16/16 checks passing  
**Ledger head:** `f2daaf2a0f1103b1b92be7c0b85cb07ec7cca312093eaa1d7392785bb22e5874`  
**Date:** October 2026

## Position

ALAVETELI is packaged for offline deployment with a verifiable audit trail. The
ethical questions this raises are answered by making the system's behaviour
checkable rather than by policy statements.

## The four commitments

1. **No hidden egress.** The deployment has no external API dependency; this is
   testable by running it with the network disconnected.
2. **Attributable output.** Every artifact is recorded in a hash chain, so what
   the system produced can be reconstructed.
3. **Operator control.** The institution owns the hardware and the keys.
4. **Refusal to overclaim.** Where a certification is not held, the project says
   so rather than implying it.

## Dual use

This project is packaged for civilian and public-sector deployment. Where an
upstream has dual-use characteristics, the licence gate and the reference-only
marking in `BENCH.json` record that.
