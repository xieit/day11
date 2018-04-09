import os, sys, time
sys.path.append(os.getcwd())

from base.base_action import BaseAction

from selenium.webdriver.common.by import By

class FilePage(BaseAction):

    # 操作按钮
    operation_button = By.XPATH, "content-desc,操作"

    # 属性
    property_button = By.XPATH, "text,属性"

    # 刷新
    refresh_button = By.XPATH, "text,刷新"

    # 新建文件夹
    new_dir_button = By.XPATH, "text,新建文件夹"

    # 新建文件
    new_file_button = By.XPATH, "text,新建文件"

    # 全部选择
    all_select_button = By.XPATH, "text,全部选择"

    # 取消全选
    all_deselect_button = By.XPATH, "text,取消全选"

    # 添加到书签
    add_mark_button = By.XPATH, "text,添加到书签"

    # 添加快捷方式
    add_shortcut_button = By.XPATH, "text,添加快捷方式"

    # set_as_home
    set_as_home_button = By.XPATH, "text,Set,1"

    # first_edit_text(文件夹和文件都可以用)
    first_edit_text = By.CLASS_NAME, "android.widget.EditText"

    # ok
    ok_button = By.XPATH, "text,确定"

    # cacnel
    cancel_button = By.XPATH, "text,取消"

    # 侧边栏按钮
    side_menu_button = By.ID, "android:id/home"
    
    # sdcard 特征
    sdcard_button = By.XPATH, "text,内部存储设备"

    # 移动选择项
    move_select_button = By.XPATH, "text,移动选择项"

    # 已存在 特征
    already_exist = By.XPATH, "text,已存在,1"

    # 文件名的特征
    file_loc = By.ID, "com.cyanogenmod.filemanager:id/navigation_view_item_name"

    # 点击操作
    def click_operation(self):
        self.click(self.operation_button)

    # 点击属性
    def click_property(self):
        self.click(self.property_button)

    # 刷新
    def click_refresh(self):
        self.click(self.refresh_button)

    # 新建文件夹
    def click_new_dir(self):
        self.click(self.new_dir_button)

    # 新建文件
    def click_new_file(self):
        self.click(self.new_file_button)

    # 全部选择
    def click_all_select(self):
        self.click(self.all_select_button)

    # 取消全选
    def click_all_deselect(self):
        self.click(self.all_deselect_button)

    # 添加到书签
    def click_add_mark(self):
        self.click(self.add_mark_button)

    # 添加快捷方式
    def click_add_shortcut(self):
        self.click(self.add_shortcut_button)

    # set_as_home
    def click_set_as_home(self):
        self.click(self.set_as_home_button)

    # 点击移动选择项
    def click_move_select(self):
        self.click(self.move_select_button)

    # 根据文件名创建对应的文件夹
    def create_dir_with_name(self, dir_name):
        self.click_operation()
        self.click_new_dir()
        self.clear_text_input_text(self.first_edit_text, dir_name)

        try:
            self.find_element(self.already_exist)
            self.click(self.cancel_button)
            self.click(self.cancel_button)
        except Exception:
            self.click(self.ok_button)
        time.sleep(1)

    # 根据文件名创建对应的文件
    def create_file_with_name(self, file_name):
        self.click_operation()
        self.click_new_file()
        self.clear_text_input_text(self.first_edit_text, file_name)

        try:
            self.find_element(self.already_exist)
            self.click(self.cancel_button)
            self.click(self.cancel_button)
            return False
        except Exception:
            self.click(self.ok_button)
            return True
        time.sleep(1)

    def is_file_already_exist(self, file_name):
        return not self.create_file_with_name(file_name)

    def clear_text_input_text(self, loc, text):
        self.clear_text(loc)
        self.input_text(loc, text)

    # 根据名字进入对应的文件夹
    def entry_dir_with_name(self, dir_name):
        loc = By.XPATH, "text," + dir_name
        self.scroll_page_until_loc(loc)
        self.click(loc)

    def entry_sdcard(self):
        self.click(self.side_menu_button)
        time.sleep(1)
        self.click(self.sdcard_button)

    def get_current_first_dir_name(self):
        return self.find_element(self.file_loc).get_attribute("text")





