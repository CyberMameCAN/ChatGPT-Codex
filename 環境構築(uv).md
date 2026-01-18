# uvでPythonの環境構築

## 新規の場合

```cd my_project_dir
uv init
```
### pip追加例

```uv add torch numpy pandas pyyaml```

## プロジェクトの続きからの場合

#### 1. プロジェクトディレクトリに移動
```cd my_project_dir```

### 2. 既存の.venvがあれば削除
```rm -rf .venv```

### 3. 3.12で新しく仮想環境を作成
```uv venv 3.12.8```

### 4. 仮想環境を有効化
```source .venv/bin/activate  # fishならactivate.fish```

### 5. pythonバージョンを確認
```python --version```

### 6. パッケージをインストール
```uv pip install -r requirements.txt```

