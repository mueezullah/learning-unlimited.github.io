#!/usr/bin/env python3
"""
Simple development server for Learning Unlimited Jekyll site.
Serves static files and basic markdown rendering.
"""

import os
import sys
import markdown
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import unquote

PROJECT_ROOT = Path(__file__).parent
PORT = 4000


class MarkdownHandler(SimpleHTTPRequestHandler):
    """Handler that serves markdown files as HTML and static files."""

    def do_GET(self):
        """Handle GET requests."""
        # Decode the URL
        path = unquote(self.path)
        
        # Handle root path
        if path == "/" or path == "/index.html":
            self.serve_file(PROJECT_ROOT / "index.html")
            return

        # Try to find the file
        file_path = PROJECT_ROOT / path.lstrip("/")
        
        # Check if it's a directory and look for index.md or index.html
        if file_path.is_dir():
            for index_file in ["index.md", "index.html"]:
                index_path = file_path / index_file
                if index_path.exists():
                    if index_file.endswith(".md"):
                        self.serve_markdown(index_path)
                    else:
                        self.serve_file(index_path)
                    return
            
            # Directory listing
            self.list_directory(file_path)
            return

        # Check for .md file if .html is requested
        if path.endswith(".html"):
            md_path = file_path.with_suffix(".md")
            if md_path.exists():
                self.serve_markdown(md_path)
                return

        # Check for markdown file directly
        if path.endswith(".md"):
            if file_path.exists():
                self.serve_markdown(file_path)
                return

        # Serve static file if it exists
        if file_path.exists():
            self.serve_file(file_path)
            return

        # Try adding .html
        html_path = file_path.with_suffix(".html")
        if html_path.exists():
            self.serve_file(html_path)
            return

        # Try adding /index.html
        index_path = file_path / "index.html"
        if index_path.exists():
            self.serve_file(index_path)
            return

        # Try adding /index.md
        md_index_path = file_path / "index.md"
        if md_index_path.exists():
            self.serve_markdown(md_index_path)
            return

        # Not found
        self.send_error(404)

    def serve_file(self, file_path):
        """Serve a static file."""
        try:
            self.send_response(200)
            
            # Determine content type
            if file_path.suffix == ".html":
                self.send_header("Content-type", "text/html; charset=utf-8")
            elif file_path.suffix == ".css":
                self.send_header("Content-type", "text/css; charset=utf-8")
            elif file_path.suffix == ".js":
                self.send_header("Content-type", "application/javascript; charset=utf-8")
            elif file_path.suffix == ".json":
                self.send_header("Content-type", "application/json; charset=utf-8")
            elif file_path.suffix == ".md":
                self.send_header("Content-type", "text/markdown; charset=utf-8")
            else:
                self.send_header("Content-type", "application/octet-stream")
            
            self.end_headers()
            
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
        except Exception as e:
            self.send_error(500, str(e))

    def serve_markdown(self, file_path):
        """Serve a markdown file as HTML."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Split front matter from content
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    front_matter = parts[1]
                    markdown_content = parts[2]
                else:
                    markdown_content = content
            else:
                markdown_content = content

            # Convert markdown to HTML
            html_content = markdown.markdown(markdown_content, extensions=["extra", "codehilite"])

            # Create full HTML document
            full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learning Unlimited</title>
    <link rel="stylesheet" href="/media/css/content-pages.css">
    <link rel="stylesheet" href="/media/css/index.css">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1, h2, h3 {{ color: #333; }}
        a {{ color: #0066cc; }}
        code {{ background-color: #f4f4f4; padding: 2px 6px; border-radius: 3px; }}
        pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 3px; overflow-x: auto; }}
    </style>
</head>
<body>
    <nav style="margin-bottom: 20px; padding-bottom: 10px; border-bottom: 1px solid #ccc;">
        <a href="/">Home</a> | 
        <a href="/about/">About</a> | 
        <a href="/participate/">Get Involved</a> | 
        <a href="/becoming-a-chapter/">Start a Chapter</a> | 
        <a href="/current-programs/">Current Programs</a> | 
        <a href="/contact/">Contact</a>
    </nav>
    {html_content}
    <hr style="margin-top: 40px; border: none; border-top: 1px solid #ccc;">
    <footer style="text-align: center; color: #666; font-size: 0.9em; margin-top: 20px;">
        <p>&copy; 2026 Learning Unlimited. All rights reserved.</p>
    </footer>
</body>
</html>"""

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(full_html.encode("utf-8"))
        except Exception as e:
            self.send_error(500, str(e))

    def log_message(self, format, *args):
        """Log HTTP requests."""
        print(f"[{self.log_date_time_string()}] {format % args}")


if __name__ == "__main__":
    os.chdir(PROJECT_ROOT)
    
    # Try to change to project root
    if not (PROJECT_ROOT / "_config.yml").exists():
        print(f"Error: Could not find _config.yml in {PROJECT_ROOT}")
        print("Make sure you're running this from the project root directory.")
        sys.exit(1)

    server = HTTPServer(("localhost", PORT), MarkdownHandler)
    print(f"Starting development server at http://localhost:{PORT}/")
    print(f"Press Ctrl+C to stop the server")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
