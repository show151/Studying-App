# Studying App

このプロジェクトは、PyQt6を使用して作成されたデスクトップアプリケーションです。アプリケーションのメインウィンドウはQt Designerで設計されており、リソースはQtのリソースシステムを使用して管理されています。

## プロジェクト構成

- `src/main.py`: アプリケーションのエントリーポイント。メインウィンドウを作成し、イベントループを開始します。
- `src/ui/main_window.ui`: Qt Designerで作成されたユーザーインターフェースの定義。
- `src/resources/resources.qrc`: アプリケーションで使用するリソースの定義。
- `requirements.txt`: プロジェクトの依存関係をリストしています。
- `.vscode/launch.json`: VS Codeのデバッグ構成。

## 使用方法

1. 必要なパッケージをインストールします。
   ```
   pip install -r requirements.txt
   ```

2. アプリケーションを起動します。
   ```
   python src/main.py
   ```
