# from huskypo import logstack
# # from huskypo_extension import Page, assertion
#
#
# class MobileCommon:
#
#     def __init__(self, driver):
#         self.page = Page(driver)
#
#     def wait_screenshot(
#             self,
#             waits: bool | list | None = None,
#             case: str = 'case',
#             name: str = 'name',
#             sleep: int = 0.5,
#             to_jpg: bool = True,
#             jpg_ratio: int = 50,
#             jpg_quality: int = 50,
#             attach: bool = True,
#             attach_jpg: bool = True,
#             remove: bool = True
#     ) -> None:
#         """
#         截圖後斷言等待的元素是否有等待成功。
#         如果 `waits=None` 不會斷言等待是否成功，
#         如同一般的 save_screenshot
#
#         Usage::
#
#             # 需確認等待的元素有出現，截圖後斷言等待結果
#             waits = page.element.wait_present(reraise=False)
#             cube.wait_screenshot(waits, "testcase", "image_name")
#
#             # 或多個 waits
#             waits = []
#             waits.append(page.element1.wait_present(reraise=False))
#             waits.append(page.element2.wait_visible(reraise=False))
#             cube.wait_screenshot(waits, "testcase", "image_name")
#
#             # 如果只需要單純的截圖
#             cube.wait_screenshot(None, "testcase", "image_name")
#
#         """
#         self.page.save_screenshot(case, name, sleep, to_jpg, jpg_ratio, jpg_quality, attach, attach_jpg, remove)
#         if waits is None:
#             return None
#         if isinstance(waits, list):
#             if False in waits:
#                 index_of_false = [index for index, value in enumerate(waits) if not value]
#                 logstack.error(f'❌ 等待列表內 index {index_of_false} is False')
#                 waits = False
#             elif waits == []:
#                 logstack.error('❌ 等待列表為空list[]')
#                 waits = False
#             else:
#                 waits = True
#         if not assertion.condition(waits, log=False):
#             logstack.error(f'❌ 截圖 "{name}" 等待條件不成立')
