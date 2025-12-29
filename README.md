# 实验6：编码规范与模块化编程

## 实验目的
遵循编码标准，实现模块化开发。

## 核心任务
1. 学习Java/Python等编码规范（命名、注释、格式）
2. 基于实验5的设计，编写核心模块代码（无需完整实现，聚焦1个模块，即附上一个模块的核心代码）
3. 实现模块间接口调用，测试代码可读性与可维护性
4. 提交代码至 Git 仓库，编写 README 说明

## 实验内容

### 1. 编码规范
本实验遵循Python的PEP8编码规范，包括：
- 命名规范：变量名、函数名使用小写字母加下划线（snake_case），类名使用驼峰命名（CamelCase）
- 注释规范：为类、函数、属性添加详细的文档字符串（docstring）
- 格式规范：缩进使用4个空格，行宽不超过80个字符

### 2. 项目结构
本实验聚焦于图书管理系统的**图书模块**，项目结构如下：

```
experiment6/
├── book_management/          # 图书管理系统主目录
│   ├── __init__.py           # 包初始化文件
│   ├── models/               # 数据模型层
│   │   └── book.py           # 图书实体类
│   ├── repositories/         # 数据访问层
│   │   └── book_repository.py # 图书数据访问类
│   └── services/             # 业务逻辑层
│       └── book_service.py   # 图书服务类
├── test_book_module.py       # 图书模块测试脚本
└── README.md                 # 项目说明文档
```

### 3. 核心模块代码

#### 3.1 图书实体类（models/book.py）
定义了图书的基本属性和方法，包括：
- 属性：book_id, isbn, title, author, publisher, publish_date, category_id, price, total_quantity, available_quantity, create_time, update_time
- 方法：get_status(), update_quantity(), __str__(), to_dict()

#### 3.2 图书数据访问类（repositories/book_repository.py）
处理图书数据的增删改查操作，包括：
- save(), find_by_id(), find_by_isbn(), find_by_params(), update(), delete(), find_all()
- 使用内存存储模拟数据库操作

#### 3.3 图书服务类（services/book_service.py）
实现图书相关的业务逻辑，包括：
- add_book(), get_book_by_id(), get_book_by_isbn(), search_books(), update_book(), delete_book(), get_all_books(), borrow_book(), return_book()
- 实现了借阅和归还图书的业务逻辑

### 4. 模块测试
编写了测试脚本 `test_book_module.py`，测试图书模块的核心功能，包括：
1. 添加图书
2. 获取所有图书
3. 根据ID查找图书
4. 根据ISBN查找图书
5. 搜索图书（按书名、作者、分类）
6. 借阅图书
7. 归还图书
8. 更新图书
9. 删除图书

## 运行说明

### 1. 运行测试脚本
```bash
python test_book_module.py
```

### 2. 预期输出
```
=== 图书模块测试 ===

1. 添加图书
   成功添加图书: Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')
   成功添加图书: Book(book_id=2, title='流畅的Python', author='Luciano Ramalho', status='可借')
   成功添加图书: Book(book_id=3, title='深入理解计算机系统', author='Randal E. Bryant', status='可借')

2. 获取所有图书
   共有 3 本图书:
   Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')
   Book(book_id=2, title='流畅的Python', author='Luciano Ramalho', status='可借')
   Book(book_id=3, title='深入理解计算机系统', author='Randal E. Bryant', status='可借')

3. 根据ID查找图书
   ID为 1 的图书: Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')

4. 根据ISBN查找图书
   ISBN为 9787115546081 的图书: Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')

5. 搜索图书
   搜索书名包含'Python'的图书 (2 本):
   Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')
   Book(book_id=2, title='流畅的Python', author='Luciano Ramalho', status='可借')
   搜索作者包含'Eric'的图书 (1 本):
   Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')
   搜索分类ID为1的图书 (2 本):
   Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')
   Book(book_id=2, title='流畅的Python', author='Luciano Ramalho', status='可借')

6. 借阅图书
   借阅图书ID 1: 成功
   借阅后图书状态: Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')
   再次借阅图书ID 1: 成功
   再次借阅后图书状态: Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')

7. 归还图书
   归还图书ID 1: 成功
   归还后图书状态: Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')

8. 更新图书
   更新后图书状态: Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')

9. 删除图书
   删除图书ID 3: 成功
   删除后共有 2 本图书:
   Book(book_id=1, title='Python编程：从入门到实践', author='Eric Matthes', status='可借')
   Book(book_id=2, title='流畅的Python', author='Luciano Ramalho', status='可借')

=== 测试完成 ===
```

## 实验成果
1. **模块化设计**：实现了清晰的三层架构（模型层、数据访问层、业务逻辑层）
2. **编码规范**：遵循PEP8编码规范，代码结构清晰、可读性强
3. **完整功能**：实现了图书模块的核心功能，包括添加、查询、借阅、归还、更新和删除
4. **测试验证**：编写了完整的测试脚本，验证了所有核心功能
5. **文档完整**：为类、函数、属性添加了详细的文档字符串
