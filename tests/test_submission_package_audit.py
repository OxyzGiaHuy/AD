from scripts.audit_submission_package import _latex_word_count, audit_submission


def test_latex_word_count_ignores_commands_and_braces():
    assert _latex_word_count(r"A \textbf{short} abstract with $k=4$ and \cite{x}.") == 7


def test_submission_audit_fails_closed_on_missing_manifest_and_placeholders(tmp_path):
    (tmp_path / "sections").mkdir()
    (tmp_path / "tables").mkdir()
    (tmp_path / "main.tex").write_text("First Author\\author@example.com", encoding="utf-8")
    (tmp_path / "sections" / "abstract.tex").write_text("short abstract", encoding="utf-8")
    (tmp_path / "cover_letter.md").write_text("cover", encoding="utf-8")
    report = audit_submission(tmp_path)
    assert report["status"] == "fail"
    assert "placeholder author" in report["issues"]
    assert "placeholder email" in report["issues"]
    assert "final CPU pipeline manifest was not supplied" in report["issues"]
