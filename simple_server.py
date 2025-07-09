#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import socket
import os

def get_local_ip():
    """ローカルIPアドレスを取得"""
    try:
        # ダミーのUDP接続を作成してローカルIPを取得
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "localhost"

def main():
    PORT = 8080
    
    # カレントディレクトリをサーバーのルートに設定
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            local_ip = get_local_ip()
            
            print("✅ サーバーが起動しました!")
            print(f"📱 スマホアクセス用URL: http://{local_ip}:{PORT}")
            print(f"💻 PC用URL: http://localhost:{PORT}")
            print("🛑 停止するには Ctrl+C を押してください")
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 サーバーを停止しました")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ ポート {PORT} は既に使用されています")
            print("他のサーバーを停止してから再実行してください")
        else:
            print(f"❌ エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
