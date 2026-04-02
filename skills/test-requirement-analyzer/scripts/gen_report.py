#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成测试需求分析报告 - 外汇展业01-尽调管理 (按模块分组)"""

# 按模块分组的测试点数据
modules = {
    "FERS1001 - 尽调任务处理": [
        ("FERS1001-01", "验证尽调任务查询功能", "功能", "P0", "输入查询条件后正确显示尽调任务列表"),
        ("FERS1001-02", "验证尽调任务筛选功能", "功能", "P0", "选择一笔尽调信息后正确进入尽调详情"),
        ("FERS1001-03", "验证尽调平台跳转功能", "功能", "P0", "点击'尽调平台'正确跳转到尽调平台详情页面"),
        ("FERS1001-04", "验证尽调中任务显示", "功能", "P0", "只显示尽调中的任务，已完成的不显示"),
        ("FERS1001-05", "验证手工发起尽调功能", "功能", "P0", "可通过此模块手工发起尽调"),
    ],
    "FERS1001-1 - 尽调任务新增（问卷类）": [
        ("FERS1001-1-01", "验证新增按钮进入功能", "功能", "P0", "点击'新增'按钮正确进入尽调新增信息页面"),
        ("FERS1001-1-02", "验证展业尽调发起编号生成", "功能", "P0", "进入新增页面自动生成展业尽调发起编号"),
        ("FERS1001-1-03", "验证新增页面按钮显示规则", "功能", "P1", "点击'新增'按钮进入时隐藏'查看详情'按钮，显示'发起尽调'按钮"),
        ("FERS1001-1-04", "验证尽调已存在时处理", "功能", "P0", "尽调编号已存在时弹出尽调平台尽调页面"),
        ("FERS1001-1-05", "验证尽调不存在时处理", "功能", "P0", "尽调编号不存在时存入页面信息并弹出尽调平台页面"),
        ("FERS1001-1-06", "验证尽调状态初始值", "功能", "P1", "后台处理尽调状态系统默认为空"),
        ("FERS1001-1-07", "验证尽调状态更新为尽调中", "功能", "P0", "尽调平台返回尽调编号后自动更新状态为'1-尽调中'"),
        ("FERS1001-1-08", "验证尽调方式默认值", "功能", "P1", "尽调方式系统默认'1-人工'"),
        ("FERS1001-1-09", "验证尽调完成状态更新", "功能", "P0", "尽调结束后自动更新状态为'2-尽调完成'"),
        ("FERS1001-1-10", "验证尽调结束日期更新", "功能", "P0", "尽调完成后自动更新尽调结束日期为平台传送的结束日期"),
    ],
    "FERS1002 - 尽调信息历史查询": [
        ("FERS1002-01", "验证历史查询条件输入", "功能", "P0", "可正确输入查询条件"),
        ("FERS1002-02", "验证历史查询结果输出", "功能", "P0", "正确显示查询结果列表"),
        ("FERS1002-03", "验证详情查看功能", "功能", "P0", "点击'详情'正确查看尽调详情页面"),
        ("FERS1002-04", "验证尽调平台跳转功能", "功能", "P1", "点击'尽调平台'按钮正确跳转到客户尽职调查平台"),
    ],
    "FERS1002-1 - 尽调任务详情（要素类）": [
        ("FERS1002-1-01", "验证要素类尽调结果查看", "功能", "P1", "可查看要素类尽调平台返回的本地结果"),
        ("FERS1002-1-02", "验证详情页面信息不可修改", "功能", "P1", "进入页面后所有信息不可输入"),
    ],
    "边界测试": [
        ("B001", "验证查询条件为空时查询", "边界", "P1", "查询条件为空时应有相应处理或提示"),
        ("B002", "验证尽调编号边界", "边界", "P1", "尽调编号长度达到最大限制时的处理"),
        ("B003", "验证无历史数据时查询", "边界", "P1", "查询无结果时的提示信息"),
    ],
    "异常测试": [
        ("E001", "验证尽调平台返回超时", "异常", "P1", "尽调平台响应超时的处理"),
        ("E002", "验证网络异常时发起尽调", "异常", "P1", "网络异常情况下的错误提示"),
        ("E003", "验证尽调平台返回异常状态", "异常", "P1", "尽调平台返回非正常状态时的处理"),
    ],
    "安全测试": [
        ("P001", "验证用户权限控制", "安全", "P0", "根据2.3用户权限控制功能访问"),
        ("P002", "验证未授权访问拦截", "安全", "P0", "未授权用户无法访问相关功能"),
    ],
}

# 场景测试点
scenarios = [
    ("SC001", "验证完整尽调流程场景", "场景", "P0", "客户发起尽调 → 系统筛选 → 业务手工发起 → 尽调平台处理 → 状态自动更新 → 尽调完成"),
    ("SC002", "验证问卷类尽调新增场景", "场景", "P0", "业务人员手工新增问卷类尽调任务 → 生成编号 → 发起尽调 → 平台返回 → 状态更新"),
    ("SC003", "验证历史查询与详情查看场景", "场景", "P1", "查询尽调历史 → 查看详情 → 跳转到尽调平台查看完整信息"),
    ("SC004", "验证要素类尽调结果查看场景", "场景", "P1", "查看要素类尽调平台返回的本地结果 → 信息只读不可修改"),
]

# 风险评估
risks = [
    ("高", "状态自动更新依赖", "尽调状态自动更新依赖尽调平台返回结果，平台异常可能导致状态不一致", "高", "增加超时处理和重试机制，状态异常时人工介入"),
    ("中", "权限控制依赖", "功能权限依赖于2.3用户权限文档，需确认权限配置完整性", "中", "与权限文档交叉验证，确保权限控制覆盖所有功能点"),
]

# 统计
total_func = sum(len(v) for k, v in modules.items() if k not in ["边界测试", "异常测试", "安全测试"])
total_bound = len(modules.get("边界测试", []))
total_excpt = len(modules.get("异常测试", []))
total_secur = len(modules.get("安全测试", []))
total_scen = len(scenarios)
total_all = sum(len(v) for v in modules.values()) + len(scenarios)

p0_count = sum(1 for v in modules.values() for t in v if t[2] == "P0") + sum(1 for s in scenarios if s[2] == "P0")
p1_count = sum(1 for v in modules.values() for t in v if t[2] == "P1") + sum(1 for s in scenarios if s[2] == "P1")

html = """<!DOCTYPE html>
<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel">
<head>
    <meta charset="UTF-8">
    <title>外汇展业01-尽调管理 - 测试需求分析报告</title>
    <!--[if gte mso 9]>
    <xml>
        <x:ExcelWorkbook>
            <x:ExcelWorksheets>
                <x:ExcelWorksheet><x:Name>测试范围分析</x:Name><x:WorksheetOptions><x:Selected/><x:FreezePanes/></x:WorksheetOptions></x:ExcelWorksheet>
                <x:ExcelWorksheet><x:Name>测试场景</x:Name><x:WorksheetOptions><x:FreezePanes/></x:WorksheetOptions></x:ExcelWorksheet>
                <x:ExcelWorksheet><x:Name>风险评估</x:Name><x:WorksheetOptions><x:FreezePanes/></x:WorksheetOptions></x:ExcelWorksheet>
                <x:ExcelWorksheet><x:Name>测试策略</x:Name><x:WorksheetOptions><x:FreezePanes/></x:WorksheetOptions></x:ExcelWorksheet>
            </x:ExcelWorksheets>
        </x:ExcelWorkbook>
    </xml>
    <![endif]-->
    <style>
        body { font-family: 'Microsoft YaHei', Arial, sans-serif; margin: 40px; }
        h1 { text-align: center; color: #333; font-size: 24px; }
        h2 { color: #333; border-left: 5px solid #4CAF50; padding-left: 10px; margin-top: 30px; }
        h3 { color: #555; margin-top: 20px; }
        .meta { text-align: center; color: #666; margin-bottom: 20px; }
        .summary { background-color: #e8f5e9; padding: 20px; margin: 20px 0; border-radius: 5px; }
        .summary ul { margin: 10px 0; }
        .summary li { margin: 5px 0; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #000; padding: 10px 8px; text-align: left; font-size: 12px; }
        th { background-color: #4CAF50; color: white; font-weight: bold; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        tr:hover { background-color: #f1f1f1; }
        .module-header { background-color: #e3f2fd; font-weight: bold; }
        .priority-p0 { background-color: #ffebee; }
        .priority-p1 { background-color: #fff3e0; }
        .priority-p2 { background-color: #e8f5e9; }
        .risk-high { background-color: #ffcdd2; font-weight: bold; }
        .risk-medium { background-color: #ffe0b2; }
        .risk-low { background-color: #c8e6c9; }
        .sheet-title { font-size: 16px; font-weight: bold; margin: 25px 0 10px 0; color: #333; border-left: 5px solid #4CAF50; padding-left: 10px; }
        .module-title { font-size: 14px; font-weight: bold; margin: 20px 0 5px 0; color: #1976D2; background-color: #e3f2fd; padding: 8px 10px; border-left: 4px solid #1976D2; }
    </style>
</head>
<body>
    <h1>外汇展业01-尽调管理 - 测试需求分析报告</h1>
    <p class="meta">生成时间：2026-03-27</p>
    
    <div class="summary">
        <h3>📊 报告摘要</h3>
        <ul>
            <li><strong>需求文档：</strong> 外汇展业01-尽调管理.docx</li>
            <li><strong>功能模块：</strong> 4 个</li>
            <li><strong>测试点总数：</strong> """ + str(total_all) + """ 个</li>
            <li><strong>功能测试点：</strong> """ + str(total_func) + """ 个</li>
            <li><strong>边界测试点：</strong> """ + str(total_bound) + """ 个</li>
            <li><strong>异常测试点：</strong> """ + str(total_excpt) + """ 个</li>
            <li><strong>安全测试点：</strong> """ + str(total_secur) + """ 个</li>
            <li><strong>场景测试点：</strong> """ + str(total_scen) + """ 个</li>
            <li><strong>优先级分布：</strong> P0: """ + str(p0_count) + """ | P1: """ + str(p1_count) + """</li>
            <li><strong>风险项：</strong> """ + str(len(risks)) + """ 个</li>
        </ul>
    </div>

    <!-- 工作表 1: 测试范围分析 (按模块分组) -->
    <div class="sheet-title">📋 工作表 1：测试范围分析（按模块分组）</div>
"""

# 按模块分组输出
for module_name, test_list in modules.items():
    html += f'    <div class="module-title">{module_name}</div>\n'
    html += """    <table>
        <thead>
            <tr>
                <th>测试点编号</th>
                <th>测试点名称</th>
                <th>测试内容描述</th>
                <th>优先级</th>
                <th>测试类型</th>
            </tr>
        </thead>
        <tbody>
"""
    for tp in test_list:
        priority_class = "priority-p0" if tp[2] == "P0" else ("priority-p1" if tp[2] == "P1" else "priority-p2")
        html += f"""            <tr class="{priority_class}">
                <td>{tp[0]}</td>
                <td>{tp[1]}</td>
                <td>{tp[4]}</td>
                <td>{tp[2]}</td>
                <td>{tp[3]}</td>
            </tr>
"""
    html += "        </tbody>\n    </table>\n"

html += """    <!-- 工作表 2: 测试场景 -->
    <div class="sheet-title">📋 工作表 2：测试场景分析</div>
    <table>
        <thead>
            <tr>
                <th>场景编号</th>
                <th>场景名称</th>
                <th>场景描述</th>
                <th>优先级</th>
                <th>测试类型</th>
            </tr>
        </thead>
        <tbody>
"""
for sc in scenarios:
    priority_class = "priority-p0" if sc[2] == "P0" else ("priority-p1" if sc[2] == "P1" else "priority-p2")
    html += f"""            <tr class="{priority_class}">
                <td>{sc[0]}</td>
                <td>{sc[1]}</td>
                <td>{sc[4]}</td>
                <td>{sc[2]}</td>
                <td>{sc[3]}</td>
            </tr>
"""

html += """        </tbody>
    </table>

    <!-- 工作表 3: 风险评估 -->
    <div class="sheet-title">📋 工作表 3：风险评估</div>
    <table>
        <thead>
            <tr>
                <th>风险等级</th>
                <th>风险项</th>
                <th>风险描述</th>
                <th>影响程度</th>
                <th>缓解措施</th>
            </tr>
        </thead>
        <tbody>
"""
for r in risks:
    risk_class = "risk-high" if r[0] == "高" else ("risk-medium" if r[0] == "中" else "risk-low")
    html += f"""            <tr class="{risk_class}">
                <td>{r[0]}</td>
                <td>{r[1]}</td>
                <td>{r[2]}</td>
                <td>{r[3]}</td>
                <td>{r[4]}</td>
            </tr>
"""

html += """        </tbody>
    </table>

    <!-- 工作表 4: 测试策略 -->
    <div class="sheet-title">📋 工作表 4：测试策略</div>
    <table>
        <thead>
            <tr>
                <th>类别</th>
                <th>项目</th>
                <th>内容/方案</th>
                <th>覆盖范围/要求</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>功能测试</td><td>正常流程验证</td><td>验证各功能模块的正常业务流程</td><td>覆盖所有功能测试点</td></tr>
            <tr><td>边界测试</td><td>边界条件验证</td><td>验证空值、边界值、超长输入等边界条件</td><td>覆盖所有边界测试点</td></tr>
            <tr><td>异常测试</td><td>异常场景验证</td><td>验证网络异常、超时、系统异常等场景</td><td>覆盖所有异常测试点</td></tr>
            <tr><td>安全测试</td><td>权限控制验证</td><td>验证用户权限控制和未授权访问拦截</td><td>覆盖所有安全测试点</td></tr>
            <tr><td>场景测试</td><td>端到端流程验证</td><td>验证完整业务流程的端到端场景</td><td>覆盖所有场景测试点</td></tr>
            <tr><td>测试数据</td><td>测试数据准备</td><td>准备测试账号、不同状态尽调数据、历史记录等</td><td>满足各测试点数据需求</td></tr>
            <tr><td>环境依赖</td><td>测试环境</td><td>尽调平台联调环境、权限配置环境</td><td>支持功能及集成测试</td></tr>
        </tbody>
    </table>

    <div class="summary">
        <h3>📊 测试维度覆盖检查</h3>
        <ul>
            <li>✅ 功能测试：""" + str(total_func) + """ 个测试点</li>
            <li>✅ 边界测试：""" + str(total_bound) + """ 个测试点</li>
            <li>✅ 异常测试：""" + str(total_excpt) + """ 个测试点</li>
            <li>✅ 安全测试：""" + str(total_secur) + """ 个测试点</li>
            <li>✅ 场景测试：""" + str(total_scen) + """ 个场景</li>
            <li>⚠️ 风险项：""" + str(len(risks)) + """ 个</li>
        </ul>
    </div>
</body>
</html>
"""

output_path = '/home/xmb-user/.openclaw/workspace/外汇展业01-尽调管理-测试需求分析报告.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"报告已生成: {output_path}")