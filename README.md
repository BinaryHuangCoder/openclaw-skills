# OpenClaw 公共技能仓库

这是OpenClaw的公共技能仓库，提供各种开箱即用的技能扩展。

## 安装使用
用户只需要对自己的OpenClaw说：`安装【技能名称】技能`，即可自动从本仓库下载安装使用，无需任何手动配置。

## 现有技能列表
| 技能ID | 技能名称 | 版本 | 描述 |
| --- | --- | --- | --- |
| requirement-to-uat-cases | 需求转UAT测试案例工具 | v1.0.0 | 读取Word格式的银行业务需求文档，自动生成符合银行规范的用户验收测试（UAT）案例，支持批量处理，减少业务人员手动编写工作量 |

## 目录结构
```
openclaw-skills/
├── README.md # 项目总说明
├── manifest.json # 技能清单索引（核心文件，自动生成）
├── .gitignore
└── skills/ # 所有技能存放目录，按功能领域分类
    ├── business-testing/ # 业务测试领域技能
    │   └── requirement-to-uat-cases/ # 需求转UAT测试案例技能
    │       ├── skill.json # 技能元数据
    │       ├── src/ # 源代码
    │       ├── config/ # 配置文件示例
    │       ├── docs/ # 技能专用文档
    │       └── tests/ # 单元测试
    ├── data-processing/ # 数据处理领域技能
    ├── api-integration/ # API集成领域技能
    └── ... # 其他领域技能
```