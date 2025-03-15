@echo off
echo 正在检查虚拟环境...

if not exist venv (
    echo 正在创建虚拟环境...
    python -m venv venv
    echo 正在安装依赖...
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
)

echo.
echo 正在激活虚拟环境...
call venv\Scripts\activate.bat

echo.
echo 正在启动 StarLabs Monad 机器人...
python main.py
pause
