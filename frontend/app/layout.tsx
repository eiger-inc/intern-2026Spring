import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Intern Development Environment',
  description: 'インターン生向け開発環境',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ja">
      <body className="bg-white text-gray-900 min-h-screen">
        {children}
      </body>
    </html>
  );
}
