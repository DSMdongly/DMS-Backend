from tests.v1.views.admin.apply import ExcelDownloadTCBase


class TestStayDownload(ExcelDownloadTCBase):
    """
    TC about stay excel download

    This TC tests
        * GET /admin/stay
    """
    def test(self):
        """
        - Test
        self.test_real()

        - Exception Test
        None
        """
        # -- Test --
        self._test('/admin/stay')
        # -- Test --
