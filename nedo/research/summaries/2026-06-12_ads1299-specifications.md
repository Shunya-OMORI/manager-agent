# ADS1299 公式仕様

## Source

- Title: ADS1299 Low-Noise, 8-Channel, 24-Bit Analog-to-Digital Converter for Biopotential Measurements
- URL or PDF: https://www.ti.com/product/ADS1299
- Authors / Organization: Texas Instruments
- Date: 2017（データシート Rev. C）
- Accessed: 2026-06-12
- Source type: official document

## Reliability

- Reliability: high
- Reason: 半導体メーカーが公開する製品ページ及び公式データシートであるため．

## Summary

ADS1299 は，EEG を含む生体電位計測向けの8チャネル同時サンプリング24 bit ADCである．プログラマブルゲインアンプ，内部基準，発振器，リードオフ検出等を内蔵し，250 SPS から16 kSPSのデータレートに対応する．

## Useful Claims

- ADS1299 は EEG・生体電位計測用途を想定した ADC である．
- 8チャネル，24 bit，同時サンプリングに対応する．
- データレートは250 SPSから16 kSPSである．

## Limitations

- 部品単体の仕様であり，自作基板全体の雑音，CMRR，無線遅延，安全性，信号品質を保証しない．
- 実装後の性能は基板設計，電源，電極，配線，筐体，通信方式を含めて評価する必要がある．

## Citation Candidate

Texas Instruments. (2017). ADS1299-x Low-Noise, 4-, 6-, 8-Channel, 24-Bit, Analog-to-Digital Converter for EEG and Biopotential Measurements, Rev. C.

## Related Task

- `tasks/active/nedo-proposal.md`
