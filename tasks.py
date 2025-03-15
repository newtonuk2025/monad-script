TASKS = [
    "MONADVERSE",
]

MONADVERSE = ["monadverse"]

# MAGICEDEN 仅适用于以下 NFT https://magiceden.io/mint-terminal/monad-testnet

FAUCET = [
    "faucet",
]

DUSTED = [
    "dusted",
]
"""
EN:
You can create your own task with the modules you need 
and add it to the TASKS list or use our ready-made preset tasks.

( ) - Means that all of the modules inside the brackets will be executed 
in random order
[ ] - Means that only one of the modules inside the brackets will be executed 
on random
SEE THE EXAMPLE BELOW:

RU:
Вы можете создать свою задачу с модулями, которые вам нужны, 
и добавить ее в список TASKS, см. пример ниже:

( ) - означает, что все модули внутри скобок будут выполнены в случайном порядке
[ ] - означает, что будет выполнен только один из модулей внутри скобок в случайном порядке
СМОТРИТЕ ПРИМЕР НИЖЕ:

CHINESE:
你可以创建自己的任务，使用你需要的模块，
并将其添加到TASKS列表中，请参见下面的示例：

( ) - 表示括号内的所有模块将按随机顺序执行
[ ] - 表示括号内的模块将按随机顺序执行

--------------------------------
!!! IMPORTANT !!!
EXAMPLE | ПРИМЕР | 示例:

TASKS = [
    "CREATE_YOUR_OWN_TASK",
]
CREATE_YOUR_OWN_TASK = [
    "memebridge",
    ("apriori", "magma", "shmonad"),
    ["ambient", "izumi", "bean"],
    "collect_all_to_monad",
]
--------------------------------


BELOW ARE THE READY-MADE TASKS THAT YOU CAN USE:
СНИЗУ ПРИВЕДЕНЫ ГОТОВЫЕ ПРИМЕРЫ ЗАДАЧ, КОТОРЫЕ ВЫ МОЖЕТЕ ИСПОЛЬЗОВАТЬ:
以下是您可以使用的现成任务：
"""


BRIDGE_AND_SWAPS = [
    "memebridge",
    ("izumi", "ambient", "bean", "swaps"),
    "collect_all_to_monad",
]


FULL_TASK = [
    ["izumi", "swaps", "ambient", "bean", "skip"],
    ["izumi", "swaps", "ambient", "bean", "skip", "skip", "skip"],
    ["izumi", "swaps", "ambient", "bean", "skip", "skip", "skip"],
    ["izumi", "aircraft", "lilchogstars", "bean", "swaps", "skip"],
    ["ambient", "izumi", "bean", "skip", "skip"],
    "collect_all_to_monad",
    ["apriori", "magma", "shmonad", "kintsu", "skip", "skip"],
    ["apriori", "magma", "shmonad", "kintsu", "skip"],
    ["ambient", "izumi", "bean", "magiceden", "monadking", "skip"],
    ["magiceden", "monadking", "aircraft", "skip", "skip"],
    "collect_all_to_monad",
    ["ambient", "izumi", "bean", "magiceden", "monadking", "skip"],
    ["izumi", "swaps", "ambient", "bean", "skip", "skip", "skip"],
    ["owlto", "skip", "skip"],
    ["izumi", "swaps", "ambient", "bean", "skip", "skip"],
    "logs",
]

BRIDGE_SEPOLIA_AND_CONVERT_TO_MON = [
    "testnet_bridge",
    "orbiter",
    "collect_all_to_monad",
]

SWAPS_TASK = [
    ("izumi", "ambient", "bean", "swaps"),
    "collect_all_to_monad",
]

STAKING_TASK = [
    ("apriori", "magma", "shmonad", "kintsu"),
]

EXCHANGE_TASK = [
    "cex_withdrawal",
]

EXCHANGE_AND_TESTNET_BRIDGE_TASK = [
    "cex_withdrawal",
    "testnet_bridge",
    "orbiter",
    "collect_all_to_monad",
]

EXCHANGE_AND_MEMEBRIDGE_TASK = [
    "cex_withdrawal",
    "memebridge",
]

# 水龙头相关任务
# "disperse_farm_accounts" - 从挖矿账户向主账户分发代币 | keys_for_faucet.txt -> private_keys.txt
# "disperse_from_one_wallet" - 从一个钱包向所有其他钱包分发代币 | keys_for_faucet.txt (第一个钱包) -> private_keys.txt

# 交易相关任务
# "collect_all_to_monad" - 将所有代币兑换为原生代币 (MON)
# "swaps" - testnet.monad.xyz/ 页面代币交换
# "bean" - 在 Bean DEX 上交换代币
# "ambient" - 在 Ambient DEX 上交换代币
# "izumi" - 在 Izumi DEX 上交换代币

# 质押相关任务
# "apriori" - 质押 MON 代币
# "magma" - 在 Magma 上质押 MON 代币
# "shmonad" - 在 shmonad.xyz 上购买和质押 shmon | 请查看下方设置
# "kintsu" - 在 kintsu.xyz/ 上质押 MON 代币
# "nostra" - 存款、借款、还款、提款

# 铸造相关任务
# "magiceden" - 在 magiceden.io 上铸造 NFT
# "owlto" - 在 Owlto 上部署合约
# "lilchogstars" - 在 testnet.lilchogstars.com/ 上铸造 NFT
# "demask" - 在 app.demask.finance/launchpad/0x2cdd146aa75ffa605ff7c5cc5f62d3b52c140f9c/0 上铸造 NFT
# "monadking" - 在 nerzo.xyz/monadking 上铸造 NFT
# "monadking_unlocked" - 在 www.nerzo.xyz/unlocked 上铸造 NFT
# "monadverse" - 在 monadverse.xyz 上铸造 NFT

# 充值相关任务
# "gaszip" - 通过 gaszip 从 arbitrum、optimism、base 向 monad 充值
# "orbiter" - 通过 Orbiter 从 Sepolia 向 Monad 跨链转账 ETH
# "memebridge" - 通过 memebridge 从 arbitrum、optimism、base 向 monad 充值

# 中心化交易所提现
# "cex_withdrawal" - 从中心化交易所提现代币

#GAMES
# "frontrunner" - 玩 frontrunner 游戏

# OTHER
# "logs" - 显示日志：MON 余额 | 交易次数 | 平均余额 | 平均交易次数
# "nad_domains" - 在 nad.domains 上注册随机域名
# "aircraft" - 在 aircraft.fun 上铸造 NFT
