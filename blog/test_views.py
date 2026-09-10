def test_successful_comment_submission(self):
    """Test for posting a comment on a post"""
    self.client.login(
        username="myUsername", password="myPassword")
    post_data = {
        'body': 'This is a test comment.'
    }
    response = self.client.post(reverse(
        'post_detail', args=['blog-title']), post_data)
    self.assertEqual(response.status_code, 200)
    self.assertIn(
        b'Comment submitted and awaiting approval',
        response.content
    )