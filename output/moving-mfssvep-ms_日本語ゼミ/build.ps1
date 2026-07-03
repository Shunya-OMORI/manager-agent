<#
  build.ps1 - このディレクトリの LaTeX プロジェクトをコンパイルする（Perl 不要）

  使い方:
    powershell -ExecutionPolicy Bypass -File build.ps1            # main.tex をビルド
    powershell -ExecutionPolicy Bypass -File build.ps1 -Clean     # 中間ファイル削除
    powershell -ExecutionPolicy Bypass -File build.ps1 -File foo  # foo.tex をビルド

  エンジン: uplatex（UTF-8 日本語）→ dvipdfmx で PDF 生成。
  MiKTeX が入っていれば latexmk は不要（latexmk は Perl を要求するため、
  ここでは uplatex + dvipdfmx を直接呼び出す）。
#>
param(
  [string]$File = 'main',
  [switch]$Clean
)

$ErrorActionPreference = 'Stop'
Set-Location -Path $PSScriptRoot

# MiKTeX の bin を PATH に追加（ユーザーインストール想定）
$miktexBin = Join-Path $env:LOCALAPPDATA 'Programs\MiKTeX\miktex\bin\x64'
if (-not (Test-Path (Join-Path $miktexBin 'uplatex.exe'))) {
  # フォールバック: PATH 上に uplatex があるか
  $cmd = Get-Command uplatex.exe -ErrorAction SilentlyContinue
  if ($cmd) { $miktexBin = Split-Path $cmd.Source } else {
    throw "uplatex が見つかりません。MiKTeX をインストールしてください（winget install MiKTeX.MiKTeX）。"
  }
}
$env:PATH = "$miktexBin;$env:PATH"

$base = [System.IO.Path]::GetFileNameWithoutExtension($File)

if ($Clean) {
  Get-ChildItem -Path $PSScriptRoot -Filter "$base.*" |
    Where-Object { $_.Extension -in '.aux','.log','.dvi','.toc','.out','.fls','.fdb_latexmk','.bbl','.blg' } |
    Remove-Item -Force -ErrorAction SilentlyContinue
  Write-Host "中間ファイルを削除しました。" -ForegroundColor Green
  return
}

$tex = "$base.tex"
if (-not (Test-Path $tex)) { throw "$tex が見つかりません。" }

function Invoke-Step($exe, $arguments, $label) {
  Write-Host "==> $label" -ForegroundColor Cyan
  & (Join-Path $miktexBin $exe) @arguments
  if ($LASTEXITCODE -ne 0) { throw "$label に失敗しました（exit $LASTEXITCODE）。$base.log を確認してください。" }
}

# 参照カウンタ等を安定させるため uplatex を 2 回実行
Invoke-Step 'uplatex.exe' @('-interaction=nonstopmode','-halt-on-error',$tex) "uplatex (1/2)"
Invoke-Step 'uplatex.exe' @('-interaction=nonstopmode','-halt-on-error',$tex) "uplatex (2/2)"
Invoke-Step 'dvipdfmx.exe' @("$base.dvi") "dvipdfmx"

$pdf = Join-Path $PSScriptRoot "$base.pdf"
if (Test-Path $pdf) {
  Write-Host "完了: $pdf ($([math]::Round((Get-Item $pdf).Length/1KB,1)) KB)" -ForegroundColor Green
} else {
  throw "PDF が生成されませんでした。"
}
