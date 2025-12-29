"""
图书模块测试脚本
测试图书服务的各种功能
"""
from datetime import datetime
from book_management.services.book_service import BookService


def test_book_module():
    """测试图书模块的核心功能"""
    print("=== 图书模块测试 ===\n")
    
    # 创建图书服务对象
    book_service = BookService()
    
    try:
        # 1. 添加图书
        print("1. 添加图书")
        book1 = book_service.add_book(
            isbn="9787115546081",
            title="Python编程：从入门到实践",
            author="Eric Matthes",
            publisher="人民邮电出版社",
            publish_date=datetime(2020, 1, 1),
            category_id=1,
            price=89.0,
            total_quantity=5
        )
        print(f"   成功添加图书: {book1}")
        
        book2 = book_service.add_book(
            isbn="9787111647813",
            title="流畅的Python",
            author="Luciano Ramalho",
            publisher="机械工业出版社",
            publish_date=datetime(2019, 12, 1),
            category_id=1,
            price=139.0,
            total_quantity=3
        )
        print(f"   成功添加图书: {book2}")
        
        book3 = book_service.add_book(
            isbn="9787115428028",
            title="深入理解计算机系统",
            author="Randal E. Bryant",
            publisher="人民邮电出版社",
            publish_date=datetime(2016, 1, 1),
            category_id=2,
            price=139.0,
            total_quantity=4
        )
        print(f"   成功添加图书: {book3}")
        
        print()
        
        # 2. 获取所有图书
        print("2. 获取所有图书")
        all_books = book_service.get_all_books()
        print(f"   共有 {len(all_books)} 本图书:")
        for book in all_books:
            print(f"   {book}")
        
        print()
        
        # 3. 根据ID查找图书
        print("3. 根据ID查找图书")
        found_book = book_service.get_book_by_id(book1.book_id)
        print(f"   ID为 {book1.book_id} 的图书: {found_book}")
        
        print()
        
        # 4. 根据ISBN查找图书
        print("4. 根据ISBN查找图书")
        found_book = book_service.get_book_by_isbn("9787115546081")
        print(f"   ISBN为 9787115546081 的图书: {found_book}")
        
        print()
        
        # 5. 搜索图书
        print("5. 搜索图书")
        # 按书名搜索
        search_result = book_service.search_books(title="Python")
        print(f"   搜索书名包含'Python'的图书 ({len(search_result)} 本):")
        for book in search_result:
            print(f"   {book}")
        
        # 按作者搜索
        search_result = book_service.search_books(author="Eric")
        print(f"   搜索作者包含'Eric'的图书 ({len(search_result)} 本):")
        for book in search_result:
            print(f"   {book}")
        
        # 按分类搜索
        search_result = book_service.search_books(category_id=1)
        print(f"   搜索分类ID为1的图书 ({len(search_result)} 本):")
        for book in search_result:
            print(f"   {book}")
        
        print()
        
        # 6. 借阅图书
        print("6. 借阅图书")
        borrow_result = book_service.borrow_book(book1.book_id)
        print(f"   借阅图书ID {book1.book_id}: {'成功' if borrow_result else '失败'}")
        print(f"   借阅后图书状态: {book_service.get_book_by_id(book1.book_id)}")
        
        # 再次借阅同一本书
        borrow_result = book_service.borrow_book(book1.book_id)
        print(f"   再次借阅图书ID {book1.book_id}: {'成功' if borrow_result else '失败'}")
        print(f"   再次借阅后图书状态: {book_service.get_book_by_id(book1.book_id)}")
        
        print()
        
        # 7. 归还图书
        print("7. 归还图书")
        return_result = book_service.return_book(book1.book_id)
        print(f"   归还图书ID {book1.book_id}: {'成功' if return_result else '失败'}")
        print(f"   归还后图书状态: {book_service.get_book_by_id(book1.book_id)}")
        
        print()
        
        # 8. 更新图书
        print("8. 更新图书")
        updated_book = book_service.update_book(
            book_id=book1.book_id,
            price=99.0,  # 更新价格
            total_quantity=6  # 更新总数量
        )
        print(f"   更新后图书状态: {updated_book}")
        
        print()
        
        # 9. 删除图书
        print("9. 删除图书")
        delete_result = book_service.delete_book(book3.book_id)
        print(f"   删除图书ID {book3.book_id}: {'成功' if delete_result else '失败'}")
        
        # 查看删除后的图书列表
        all_books = book_service.get_all_books()
        print(f"   删除后共有 {len(all_books)} 本图书:")
        for book in all_books:
            print(f"   {book}")
        
        print()
        
        print("=== 测试完成 ===")
        
    except Exception as e:
        print(f"测试过程中发生错误: {e}")


if __name__ == "__main__":
    test_book_module()
