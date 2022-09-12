def test_search_website(google_page, time24_page):
    google_page.open()
    assert google_page.is_current_page(), "Google page is not opened"

    website_url = "time24.com"
    google_page.search_input.send_keys(website_url)
    google_page.search_input.submit()
    assert len(google_page.search_results) > 0, "Search not executed"

    suggestions = google_page.get_search_results_by_text(website_url)
    assert len(suggestions) > 0, f"Links for '{website_url}' not found"

    suggestions[0].click()
    assert time24_page.is_current_page(), f"Page {website_url} not opened"
