# 成竹東砂鍼灸整骨院 - 整体サブスク LP

## 概要
成竹東砂鍼灸整骨院の整体サブスクリプションサービス用ランディングページです。

## セットアップ手順

### 1. Meta Pixel設定
✅ **設定完了** - Pixel ID: `1373667297066608` が設定済みです。

```html
<!-- 25行目と29行目 -->
fbq('init', '1373667297066608');
<!-- 30行目 -->
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=1373667297066608&ev=PageView&noscript=1"/></noscript>
```

### 2. Google Analytics設定
`index.html`の以下の箇所を実際の測定IDに置き換えてください：

```html
<!-- 9行目と14行目 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
gtag('config', 'G-XXXXXXXXXX');
```

### 3. LINE公式アカウント設定
`index.html`の以下の箇所を実際のLINE URLに置き換えてください：

```html
<!-- 107行目、229行目、238行目 -->
<a href="https://lin.ee/YOUR_LINE_ID_HERE" target="_blank" rel="noopener">
```

### 4. 院の詳細情報設定
`index.html`の233-236行目の院情報を実際の情報に更新してください：

```html
<h3 class="text-2xl font-bold mb-6">成竹東砂鍼灸整骨院</h3>
<p class="mb-2">📍 東京都江東区東砂7‑XX‑XX（東砂駅から徒歩X分）</p>
<p class="mb-2">📞 03‑XXXX‑XXXX</p>
<p class="mb-6">🕒 平日 9:00‑12:30 / 15:00‑20:00｜土曜 9:00‑12:00 / 14:00‑18:00｜日祝休</p>
```

## ローカル開発サーバー起動

```bash
python3 simple_server.py
```

サーバー起動後、以下のURLでアクセス可能：
- PC: http://localhost:8080
- スマホ: http://[表示されるローカルIP]:8080

## 主な変更点（元のLPとの違い）

1. **院名**: 成竹鍼灸整骨院 → 成竹東砂鍼灸整骨院
2. **対象地域**: 南砂町周辺 → 東砂・大島周辺
3. **Meta Pixel ID**: 新しいIDに設定（要更新）
4. **Google Analytics ID**: 新しいIDに設定（要更新）
5. **LINE公式アカウント**: 新しいアカウントに設定（要更新）
6. **住所・電話番号**: 東砂の情報に更新（要更新）

## GitHub Pages設定手順

### リポジトリ作成後の設定
1. GitHubリポジトリの「Settings」タブをクリック
2. 左サイドバーの「Pages」をクリック
3. Source で「Deploy from a branch」を選択
4. Branch で「main」を選択、フォルダは「/ (root)」を選択
5. 「Save」をクリック
6. 数分後に `https://[USERNAME].github.io/higashisunaseitailp/` でアクセス可能

### Meta Pixel動作確認
- GitHub Pagesデプロイ後、Meta Pixel Helperで「Pixel ID: 1373667297066608」が検出されることを確認
- コンバージョントラッキングも正常に動作します

## 注意事項

- ✅ Meta Pixel ID設定完了（1373667297066608）
- ⏳ Google Analytics ID要設定（G-XXXXXXXXXX）
- ⏳ LINE公式アカウントURL要設定
- ⏳ 院の詳細情報要更新
