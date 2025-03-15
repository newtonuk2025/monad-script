@echo off
echo ====================================
echo Monad 主工具更新程序
echo ====================================
echo.

:: 安全提示：此更新程序不会上传您的私钥
:: 所有操作都在您的本地 PC 上执行

:: 检查是否安装了 git
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo 未安装 Git。请安装 Git 以使用此更新程序。
    goto end
)

:: 检查 .git 目录是否存在
if not exist .git (
    echo 这不是一个 git 仓库。请先克隆仓库。
    goto end
)

:: 备份重要的数据文件
echo 正在备份您的数据文件...
if not exist backup mkdir backup
if exist data\private_keys.txt copy /Y data\private_keys.txt backup\private_keys.txt
if exist data\proxies.txt copy /Y data\proxies.txt backup\proxies.txt
if exist data\twitter_tokens.txt copy /Y data\twitter_tokens.txt backup\twitter_tokens.txt
if exist data\keys_for_faucet.txt copy /Y data\keys_for_faucet.txt backup\keys_for_faucet.txt
if exist data\discord_tokens.txt copy /Y data\discord_tokens.txt backup\discord_tokens.txt
if exist data\email_tokens.txt copy /Y data\email_tokens.txt backup\email_tokens.txt

:: 备份配置文件（仅供参考，不会恢复）
echo 正在备份配置文件（仅供参考）...
if exist config.yaml copy /Y config.yaml backup\config.yaml
if exist tasks.py copy /Y tasks.py backup\tasks.py

:: 从 GitHub 获取最新更改
echo 正在从 GitHub 获取最新更改...
git fetch origin main
if %ERRORLEVEL% NEQ 0 (
    echo 获取更新失败。请检查您的网络连接。
    goto end
)

:: 确保 tasks.py 和 config.yaml 被跟踪且未被忽略
echo 确保配置文件未被忽略...
git update-index --no-assume-unchanged tasks.py config.yaml 2>nul

:: 强制重置以匹配 GitHub 版本（这将覆盖除 .gitignore 中文件外的所有文件）
echo 正在应用 GitHub 更新（覆盖本地更改）...
git reset --hard origin/main

:: 从 GitHub 显式检出 tasks.py 和 config.yaml 以确保它们已更新
echo 确保 tasks.py 和 config.yaml 已从 GitHub 更新...
git checkout origin/main -- tasks.py config.yaml

:: 恢复数据文件（这些不会受到 GitHub 更改的影响）
echo 正在恢复您的数据文件...
if exist backup\private_keys.txt copy /Y backup\private_keys.txt data\private_keys.txt
if exist backup\proxies.txt copy /Y backup\proxies.txt data\proxies.txt
if exist backup\twitter_tokens.txt copy /Y backup\twitter_tokens.txt data\twitter_tokens.txt
if exist backup\keys_for_faucet.txt copy /Y backup\keys_for_faucet.txt data\keys_for_faucet.txt
if exist backup\discord_tokens.txt copy /Y backup\discord_tokens.txt data\discord_tokens.txt
if exist backup\email_tokens.txt copy /Y backup\email_tokens.txt data\email_tokens.txt

echo.
echo 更新成功完成！
echo.
echo - 您的数据文件已被保留
echo - 配置文件（tasks.py、config.yaml）已被替换为 GitHub 版本
echo - 旧配置备份在 backup\tasks.py 和 backup\config.yaml 中
echo - 所有冲突都已通过使用 GitHub 版本解决

:end
echo.