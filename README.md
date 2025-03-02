  # The  Company Website

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Gmail SMTP](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)

一个使用Streamlit构建的现代化企业展示网站，包含团队介绍和邮件联系功能。

## ✨ 主要功能
- **响应式布局**：三栏式团队展示适配不同屏幕尺寸
- **动态内容加载**：通过CSV文件管理团队数据
- **安全邮件系统**：
  - 带正则验证的邮箱格式检查
  - 多主题选择功能
  - QQ邮箱 SMTP加密传输（SSL）
- **交互式UI**：
  - 智能表单验证
  - 实时反馈提示
  - 图片动态加载

## 📦 项目结构
company-website<br />
├── Home.py # 主界面入口 <br />
├── send_email.py # 邮件服务核心模块 <br />
├── pages/ <br />
│ └── Contact_Us.py # 联系页面组件 <br />
├── data.csv # 团队成员数据(姓名/职位/照片) <br />
├── topics.csv # 咨询主题选项 <br />
├── images/ # 成员照片存储目录 <br />
└── requirements.txt # 依赖清单<br />

## 🚀 快速启动
### 环境准备
bash
### 克隆项目
git clone https://github.com/Echosofreverie/company-website.git<br />
cd company-website<br />
### 创建虚拟环境（可选）
python -m venv venv <br />
source venv/bin/activate # Linux/Mac <br />
venv\Scripts\activate # Windows<br />
### 安装依赖
pip install -r requirements.txt<br />
