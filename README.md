# 神絆的導師自動化輔助腳本

版本 3.12 版

# 資料夾架構

view/：負責顯示數據（即模型）給用戶，並且可能允許用戶進行一些交互操作，比如點擊按鈕等。  
controller/：接受用戶的輸入，並根據用戶的輸入通過改變模型的狀態或者是選擇一個新的視圖來響應用戶的輸入。  
models/：存放數據模型相關的代碼，這些代碼定義了應用程序的數據結構和數據管理邏輯。  
utils/：存放應用程序中用於處理特定業務邏輯、實用函數或服務的代碼。  
static/：用於存放靜態文件，如 CSS、JavaScript 文件和圖片。  
templates/：如果您的視圖層使用了模板引擎，這裡可以存放模板文件。  
config/：存放配置文件，如數據庫配置、應用程序設置等。

# 打包成可執行檔案

```zsh
pip freeze > requirements.txt
```

```zsh
pip install -r requirements.txt
```

```zsh
pyinstaller --onefile src/main.py -w
```
