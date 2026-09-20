html_content = """<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='2' b:layoutsVersion='3' b:responsive='true' b:templateUrl='indie.xml' b:templateVersion='1.3.0' expr:dir='data:blog.languageDirection' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<head>
    <meta content='width=device-width, initial-scale=1.0' name='viewport'/>
    <b:include data='blog' name='all-head-content'/>
    <title><data:blog.pageTitle/></title>
    <b:skin><![CDATA[
        :root {
            --primary-color: #4CAF50;
            --secondary-color: #2E7D32;
            --bg-color: #f5f5f5;
            --text-color: #333;
            --card-bg: #fff;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
        }

        header {
            background-color: var(--card-bg);
            padding: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .page-container {
            max-width: 900px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .header-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 15px;
            text-decoration: none;
        }

        .brand img {
            width: 60px;
            height: 60px;
            border-radius: 12px;
        }

        .brand h1 {
            margin: 0;
            font-size: 24px;
            color: var(--secondary-color);
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-color);
            margin-left: 20px;
            font-weight: 500;
        }

        .nav-links a:hover {
            color: var(--primary-color);
        }

        .hero {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 60px 0;
            gap: 40px;
        }

        .hero-text {
            flex: 1;
        }

        .hero-text h2 {
            font-size: 3em;
            margin-bottom: 20px;
            color: var(--secondary-color);
            line-height: 1.2;
        }

        .hero-text p {
            font-size: 1.2em;
            margin-bottom: 30px;
            color: #666;
        }

        .download-btn {
            display: inline-flex;
            align-items: center;
            background-color: var(--primary-color);
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 1.1em;
            font-weight: bold;
            transition: background-color 0.3s;
        }

        .download-btn:hover {
            background-color: var(--secondary-color);
        }

        .hero-image {
            flex: 1;
            text-align: center;
        }

        .hero-image img {
            max-width: 100%;
            height: 500px;
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        }

        .features {
            background-color: var(--card-bg);
            padding: 60px 0;
        }

        .features h2 {
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 40px;
            color: var(--secondary-color);
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .feature-card {
            padding: 20px;
            border-radius: 12px;
            background: var(--bg-color);
            border-left: 4px solid var(--primary-color);
        }

        .feature-card h3 {
            margin-top: 0;
            color: var(--secondary-color);
        }

        .screenshots {
            padding: 60px 0;
        }

        .screenshots h2 {
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 40px;
            color: var(--secondary-color);
        }

        .screenshot-gallery {
            display: flex;
            overflow-x: auto;
            gap: 20px;
            padding-bottom: 20px;
            align-items: center;
        }

        .screenshot-gallery::-webkit-scrollbar {
            height: 10px;
        }

        .screenshot-gallery::-webkit-scrollbar-track {
            background: #e0e0e0;
            border-radius: 5px;
        }

        .screenshot-gallery::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 5px;
        }

        .screenshot-gallery::-webkit-scrollbar-thumb:hover {
            background: #555;
        }

        .screenshot-gallery img {
            height: 400px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        /* Post/Page Content Styles */
        .content {
            background-color: var(--card-bg);
            padding: 40px;
            margin-top: 40px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }

        .content h1, .post-title {
            color: var(--secondary-color);
            margin-top: 0;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        .content h2 {
            color: var(--secondary-color);
            margin-top: 30px;
            font-size: 1.5em;
        }

        .content h3 {
            color: var(--primary-color);
            font-size: 1.2em;
        }

        .content p {
            margin-bottom: 15px;
        }

        .content ul {
            margin-bottom: 20px;
            padding-left: 20px;
        }

        .content li {
            margin-bottom: 10px;
        }

        .date {
            color: #666;
            font-style: italic;
            margin-bottom: 20px;
        }

        footer {
            background-color: #222;
            color: #fff;
            text-align: center;
            padding: 30px 0;
            margin-top: 40px;
        }

        footer a {
            color: #ccc;
            text-decoration: none;
            margin: 0 10px;
        }

        footer a:hover {
            color: #fff;
        }

        @media (max-width: 768px) {
            .hero {
                flex-direction: column;
                text-align: center;
            }
            .nav-links {
                display: none;
            }
            .hero-text h2 {
                font-size: 2em;
            }
            .content {
                padding: 20px;
            }
        }
    ]]></b:skin>
    <b:template-skin><![CDATA[
        body#layout { padding: 0; }
    ]]></b:template-skin>
</head>
<body>
    <header>
        <div class="container header-content">
            <a expr:href='data:blog.homepageUrl' class="brand">
                <img src="https://play-lh.googleusercontent.com/MSDF7fzU7ZwOjE_Ts5ta13IXYKh2CsLsmXUwHb9TJ79S1LXCh77E_ld5827YvxKNBY-NkHvrjHozdqoAepy3XA=w240-h480" alt="Daily Expense Icon"/>
                <h1>Daily Expense</h1>
            </a>
            <nav class="nav-links">
                <a expr:href='data:blog.homepageUrl'>Home</a>
                <a expr:href='data:blog.homepageUrl + "p/privacy-policy.html"'>Privacy Policy</a>
            </nav>
        </div>
    </header>

    <b:section id='main' class='main' showaddelement='no'>
        <b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog'>
            <b:includable id='main' var='top'>
                <b:if cond='data:view.isHomepage'>
                    <!-- Homepage Landing -->
                    <section class="container hero">
                        <div class="hero-text">
                            <h2>Your Personal Expense &amp; Money Manager</h2>
                            <p>Daily Expense Manager is a simple, fast &amp; reliable money calculator. Keep an eye on all of your money related transactions. Every calculation saved offline and you can backup or restore it anytime.</p>
                            <a href="https://play.google.com/store/apps/details?id=me.raaju.expensecalculatornewone&amp;hl=en" target="_blank" class="download-btn">
                                <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;"><path d="M22.56 12.55c0-.66-.06-1.3-.17-1.92H12v3.63h5.92c-.25 1.18-.88 2.18-1.8 2.8v2.32h2.9c1.7-1.57 2.68-3.88 2.68-6.43z" fill="#4285F4" stroke="none"/><path d="M12 23.3c2.97 0 5.46-.98 7.28-2.66l-2.9-2.32c-.99.66-2.25 1.05-3.52 1.05-2.71 0-5.01-1.83-5.84-4.29H3.97v2.4C5.78 21.08 8.65 23.3 12 23.3z" fill="#34A853" stroke="none"/><path d="M6.16 15.08c-.21-.63-.33-1.3-.33-1.98s.12-1.35.33-1.98v-2.4H3.97C3.35 10.02 3 10.99 3 12s.35 1.98.97 3.28l2.19-1.7z" fill="#FBBC05" stroke="none"/><path d="M12 4.7c1.61 0 3.06.55 4.2 1.64l3.15-3.15C17.46 1.52 14.97.5 12 .5 8.65 .5 5.78 2.72 3.97 6.22l2.19 1.7C7 5.46 9.3 3.63 12 3.63z" fill="#EA4335" stroke="none"/></svg>
                                Get it on Google Play
                            </a>
                        </div>
                        <div class="hero-image">
                            <img src="https://play-lh.googleusercontent.com/sEEmV06vUKH1sjOVGCHOK4_bkPWqv5f9sMbW8Iu-ReRcBTIa9M_GXaq7v6vbdBRNUvfU-FHmL8SxrZeGuNTYvQ=w526-h296" alt="App Preview"/>
                        </div>
                    </section>

                    <section id="features" class="features">
                        <div class="container">
                            <h2>Key Features</h2>
                            <div class="feature-grid">
                                <div class="feature-card">
                                    <h3>Track Expenses &amp; Earnings</h3>
                                    <p>Calculate your expenses and earnings separately. Easily view all money transactions in one place.</p>
                                </div>
                                <div class="feature-card">
                                    <h3>Check Available Balance</h3>
                                    <p>Keep a real-time track of your available balance so you never overspend.</p>
                                </div>
                                <div class="feature-card">
                                    <h3>Weekly &amp; Monthly Reports</h3>
                                    <p>Get a comprehensive view of your finances with weekly and monthly money transaction lists.</p>
                                </div>
                                <div class="feature-card">
                                    <h3>Built-in Calculator</h3>
                                    <p>Perform calculations effortlessly within the app without needing a separate tool.</p>
                                </div>
                                <div class="feature-card">
                                    <h3>Offline &amp; Secure</h3>
                                    <p>No internet connection needed. All data is saved offline. You can backup and restore anytime.</p>
                                </div>
                                <div class="feature-card">
                                    <h3>Multi-Language Support</h3>
                                    <p>Change the app interface to your preferred language with beautiful &amp; attractive design.</p>
                                </div>
                            </div>
                        </div>
                    </section>

                    <section id="screenshots" class="screenshots container">
                        <h2>App Screenshots</h2>
                        <div class="screenshot-gallery">
                            <img src="https://play-lh.googleusercontent.com/sEEmV06vUKH1sjOVGCHOK4_bkPWqv5f9sMbW8Iu-ReRcBTIa9M_GXaq7v6vbdBRNUvfU-FHmL8SxrZeGuNTYvQ=w526-h296" alt="Screenshot 1"/>
                            <img src="https://play-lh.googleusercontent.com/lbo1fLO8fwDX7RpmbZLlDiTIueEMgBnvxOnoJ0T11ImATkbEqmKS7zFbHOE8eBrPNjOxFz3Wyxb9IbUjBdVh=w526-h296" alt="Screenshot 2"/>
                            <img src="https://play-lh.googleusercontent.com/XPreIyFQhAjum4mzcyEeUDNBO29H7kPlM2LtpkGwofWH_K_5l-qwdEipo2L2Zc6tdU1bfm-DRwoVRqTJSZrmjpY=w526-h296" alt="Screenshot 3"/>
                            <img src="https://play-lh.googleusercontent.com/BzEBnm8wK4lpaU7gbwapJjDmc_MkKol8ZLv7BtTwZSHuMN_Spsyt_kEvDch3z81xEoJNzOPc8NCF0hK_kpm1fTI=w526-h296" alt="Screenshot 4"/>
                            <img src="https://play-lh.googleusercontent.com/dFY0kbUZ_BRJ7Z3Z4XlyQj0tKDYFIodvZHqZXXd5s1JS-rE4Iv7LXnkfYVTARthmHOVUqWVQ6wRUAUdXKQqh=w526-h296" alt="Screenshot 5"/>
                            <img src="https://play-lh.googleusercontent.com/e5R9NhTgzkXT1R1DmOQNgNuJCHGkcxrQCE_Xf_3J63GZWt_sdt1bJKwKYTHhlBcAb_uposbXE2kbXMsncUQgMQ=w526-h296" alt="Screenshot 6"/>
                        </div>
                    </section>
                <b:else/>
                    <main class="page-container">
                        <div class="content">
                            <!-- include standard posts loop -->
                            <b:loop values='data:posts' var='post'>
                                <b:include data='post' name='post'/>
                            </b:loop>
                        </div>
                    </main>
                </b:if>
            </b:includable>

            <b:includable id='post' var='post'>
                <div class='post hentry uncustomized-post-template'>
                    <a expr:name='data:post.id'/>
                    <b:if cond='data:post.title'>
                        <h1 class='post-title entry-title'>
                            <b:if cond='data:post.link'>
                                <a expr:href='data:post.link'><data:post.title/></a>
                            <b:else/>
                                <b:if cond='data:post.url'>
                                    <b:if cond='data:blog.url != data:post.url'>
                                        <a expr:href='data:post.url'><data:post.title/></a>
                                    <b:else/>
                                        <data:post.title/>
                                    </b:if>
                                <b:else/>
                                    <data:post.title/>
                                </b:if>
                            </b:if>
                        </h1>
                    </b:if>

                    <div class='post-header'>
                        <div class='post-header-line-1'/>
                    </div>

                    <div class='post-body entry-content' expr:id='&quot;post-body-&quot; + data:post.id'>
                        <data:post.body/>
                        <div style='clear: both;'/> <!-- clear for photos floats -->
                    </div>

                    <div class='post-footer'>
                        <div class='post-footer-line post-footer-line-1'/>
                        <div class='post-footer-line post-footer-line-2'/>
                        <div class='post-footer-line post-footer-line-3'/>
                    </div>
                </div>
            </b:includable>

            <b:includable id='nextprev'>
              <div class='blog-pager' id='blog-pager'>
              </div>
            </b:includable>

            <b:includable id='backlinks'>
            </b:includable>

            <b:includable id='comment-form'>
            </b:includable>

            <b:includable id='backlinkDeleteIcon'>
            </b:includable>

            <b:includable id='postQuickEdit'>
            </b:includable>

            <b:includable id='shareButtons'>
            </b:includable>

            <b:includable id='status-message'>
            </b:includable>

            <b:includable id='commentDeleteIcon'>
            </b:includable>

            <b:includable id='feedLinks'>
            </b:includable>

            <b:includable id='feedLinksBody'>
            </b:includable>

            <b:includable id='comments' var='post'>
            </b:includable>
        </b:widget>
    </b:section>

    <footer>
        <div class="container">
            <p>&amp;copy; 2026 Mijanur Rahman Raju. All rights reserved.</p>
            <div style="margin-top: 10px;">
                <a expr:href='data:blog.homepageUrl'>Home</a>
                <a expr:href='data:blog.homepageUrl + "p/privacy-policy.html"'>Privacy Policy</a>
                <a href="https://play.google.com/store/apps/details?id=me.raaju.expensecalculatornewone&amp;hl=en">Google Play</a>
            </div>
        </div>
    </footer>
</body>
</html>
"""
with open('blogger-theme.xml', 'w') as f:
    f.write(html_content)
