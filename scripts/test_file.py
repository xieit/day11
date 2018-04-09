import os, sys, pytest

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.file_page import FilePage

class TestA:

    def setup(self):
        self.driver = init_driver()
        self.file_page = FilePage(self.driver)

    def test_uiautomator2(self):

        pass











# class TestFile:
#
#     def setup(self):
#         self.driver = init_driver()
#         self.file_page = FilePage(self.driver)
#
#     def test_refresh(self):
#
#         # 进入sd卡
#         # self.file_page.entry_sdcard()
#
#         # 获取当前目录第一个文件夹的名字
#         first_dir_name = self.file_page.get_current_first_dir_name()
#         # 滚动半屏
#         self.file_page.scroll_page_one_time()
#         # 获取当前目录第一个文件夹的名字 和 之前保存的对比
#         temp = self.file_page.get_current_first_dir_name()
#         if temp == first_dir_name:
#             # 如果一直，说明屏幕没有滑动，文件过少
#             assert 0, "当前滚动没有成功"
#         else:
#             # 如果不一致 点击刷新
#             self.file_page.click_operation()
#             self.file_page.click_refresh()
#
#
#         # 判断当前目录第一个文件夹的名字 和 之前保存的对比
#         after_first_dir_name = self.file_page.get_current_first_dir_name()
#         assert first_dir_name == after_first_dir_name
#
#
#     @pytest.mark.skipif(True, reason="done")
#     def test_first(self):
#
#         # 创建zzz
#         self.file_page.create_dir_with_name("zzz")
#         # 创建aaa
#         self.file_page.create_dir_with_name("aaa")
#         # 进入zzz
#         self.file_page.entry_dir_with_name("zzz")
#         # 创建1-20.txt
#         for i in range(20):
#             self.file_page.create_file_with_name(str(i + 1) + ".txt")
#         # 全选
#         self.file_page.click_operation()
#         self.file_page.click_all_select()
#
#         # 进入aaa
#         self.file_page.entry_sdcard()
#         self.file_page.entry_dir_with_name("aaa")
#
#         # 移动选择项
#         self.file_page.click_operation()
#         self.file_page.click_move_select()
#         self.file_page.create_dir_with_name("zzz")
#         # 创建aaa
#         self.file_page.create_dir_with_name("aaa")
#         # 进入zzz
#         self.file_page.entry_dir_with_name("zzz")
#         # 创建1-20.txt
#         for i in range(20):
#             self.file_page.create_file_with_name(str(i + 1) + ".txt")
#         # 全选
#         self.file_page.click_operation()
#         self.file_page.click_all_select()
#
#         # 进入aaa
#         self.file_page.entry_sdcard()
#         self.file_page.entry_dir_with_name("aaa")
#
#         # 移动选择项
#         self.file_page.click_operation()
#         self.file_page.click_move_select()
#
#         # 验证
#         for i in range(2):
#             if self.file_page.is_file_already_exist(str(i + 1) + ".txt"):
#                 continue
#             else:
#                 assert 0
#
#         else:
#             assert 1
#             return