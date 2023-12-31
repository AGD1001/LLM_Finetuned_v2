<!DOCTYPE html>
<html class="">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
		<meta name="description" content="We’re on a journey to advance and democratize artificial intelligence through open source and open science." />
		<meta property="fb:app_id" content="1321688464574422" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:site" content="@huggingface" />
		<meta property="og:title" content="funsd.py · nielsr/funsd at main" />
		<meta property="og:type" content="website" />
		<meta property="og:url" content="https://huggingface.co/datasets/nielsr/funsd/blob/main/funsd.py" />
		<meta property="og:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/datasets/nielsr/funsd.png" />

		<link rel="stylesheet" href="/front/build/kube-72bd1c3/style.css" />

		<link rel="preconnect" href="https://fonts.gstatic.com" />
		<link
			href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap"
			rel="stylesheet"
		/>
		<link
			href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap"
			rel="stylesheet"
		/>

		<link
			rel="preload"
			href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css"
			as="style"
			onload="this.onload=null;this.rel='stylesheet'"
		/>
		<noscript>
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css" />
		</noscript>

		  <!-- HEAD_svelte-1oal594_START --><style>.blob-line-num::before {
			content: attr(data-line-num);
		}
	</style><!-- HEAD_svelte-1oal594_END -->

		<title>funsd.py · nielsr/funsd at main</title>

		<script defer data-domain="huggingface.co" src="/js/script.js"></script>
	</head>
	<body class="flex flex-col min-h-screen bg-white dark:bg-gray-950 text-black ViewerBlobPage">
		<div class="flex min-h-screen flex-col">
	<div class="SVELTE_HYDRATER contents" data-props="{&quot;classNames&quot;:&quot;&quot;,&quot;isWide&quot;:false,&quot;isZh&quot;:false}" data-target="MainHeader"><header class="border-b border-gray-100 "><div class="w-full px-4 container flex h-16 items-center"><div class="flex flex-1 items-center"><a class="mr-5 flex flex-none items-center lg:mr-6" href="/"><img alt="Hugging Face's logo" class="w-7 md:mr-2" src="/front/assets/huggingface_logo-noborder.svg">
				<span class="hidden whitespace-nowrap text-lg font-bold md:block">Hugging Face</span></a>
			<div class="relative flex-1 lg:max-w-sm mr-2 sm:mr-4 lg:mr-6"><input autocomplete="off" class="w-full dark:bg-gray-950 pl-8 form-input-alt h-9 pr-3 focus:shadow-xl" name="" placeholder="Search models, datasets, users..."  spellcheck="false" type="text" value="">
	<svg class="absolute left-2.5 text-gray-400 top-1/2 transform -translate-y-1/2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9a9 9 0 0 1-9-9z" fill="currentColor"></path></svg>
	</div>
			<div class="flex flex-none items-center justify-center p-0.5 place-self-stretch lg:hidden"><button class="relative z-30 flex h-6 w-8 items-center justify-center" type="button"><svg width="1em" height="1em" viewBox="0 0 10 10" class="text-xl" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.65039 2.9999C1.65039 2.8066 1.80709 2.6499 2.00039 2.6499H8.00039C8.19369 2.6499 8.35039 2.8066 8.35039 2.9999C8.35039 3.1932 8.19369 3.3499 8.00039 3.3499H2.00039C1.80709 3.3499 1.65039 3.1932 1.65039 2.9999ZM1.65039 4.9999C1.65039 4.8066 1.80709 4.6499 2.00039 4.6499H8.00039C8.19369 4.6499 8.35039 4.8066 8.35039 4.9999C8.35039 5.1932 8.19369 5.3499 8.00039 5.3499H2.00039C1.80709 5.3499 1.65039 5.1932 1.65039 4.9999ZM2.00039 6.6499C1.80709 6.6499 1.65039 6.8066 1.65039 6.9999C1.65039 7.1932 1.80709 7.3499 2.00039 7.3499H8.00039C8.19369 7.3499 8.35039 7.1932 8.35039 6.9999C8.35039 6.8066 8.19369 6.6499 8.00039 6.6499H2.00039Z"></path></svg>
		</button>

	</div></div>
		<nav aria-label="Main" class="ml-auto hidden lg:block"><ul class="flex items-center space-x-2"><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-indigo-700" href="/models"><svg class="mr-1.5 text-gray-400 group-hover:text-indigo-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
					Models</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-red-700" href="/datasets"><svg class="mr-1.5 text-gray-400 group-hover:text-red-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
					Datasets</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-blue-700" href="/spaces"><svg class="mr-1.5 text-gray-400 group-hover:text-blue-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 25 25"><path opacity=".5" d="M6.016 14.674v4.31h4.31v-4.31h-4.31ZM14.674 14.674v4.31h4.31v-4.31h-4.31ZM6.016 6.016v4.31h4.31v-4.31h-4.31Z" fill="currentColor"></path><path opacity=".75" fill-rule="evenodd" clip-rule="evenodd" d="M3 4.914C3 3.857 3.857 3 4.914 3h6.514c.884 0 1.628.6 1.848 1.414a5.171 5.171 0 0 1 7.31 7.31c.815.22 1.414.964 1.414 1.848v6.514A1.914 1.914 0 0 1 20.086 22H4.914A1.914 1.914 0 0 1 3 20.086V4.914Zm3.016 1.102v4.31h4.31v-4.31h-4.31Zm0 12.968v-4.31h4.31v4.31h-4.31Zm8.658 0v-4.31h4.31v4.31h-4.31Zm0-10.813a2.155 2.155 0 1 1 4.31 0 2.155 2.155 0 0 1-4.31 0Z" fill="currentColor"></path><path opacity=".25" d="M16.829 6.016a2.155 2.155 0 1 0 0 4.31 2.155 2.155 0 0 0 0-4.31Z" fill="currentColor"></path></svg>
					Spaces</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-yellow-700" href="/docs"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1.5 text-gray-400 group-hover:text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path opacity="0.5" d="M20.9022 5.10334L10.8012 10.8791L7.76318 9.11193C8.07741 8.56791 8.5256 8.11332 9.06512 7.7914L15.9336 3.73907C17.0868 3.08811 18.5002 3.26422 19.6534 3.91519L19.3859 3.73911C19.9253 4.06087 20.5879 4.56025 20.9022 5.10334Z" fill="currentColor"></path><path d="M10.7999 10.8792V28.5483C10.2136 28.5475 9.63494 28.4139 9.10745 28.1578C8.5429 27.8312 8.074 27.3621 7.74761 26.7975C7.42122 26.2327 7.24878 25.5923 7.24756 24.9402V10.9908C7.25062 10.3319 7.42358 9.68487 7.74973 9.1123L10.7999 10.8792Z" fill="currentColor" fill-opacity="0.75"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M21.3368 10.8499V6.918C21.3331 6.25959 21.16 5.61234 20.8346 5.03949L10.7971 10.8727L10.8046 10.874L21.3368 10.8499Z" fill="currentColor"></path><path opacity="0.5" d="M21.7937 10.8488L10.7825 10.8741V28.5486L21.7937 28.5234C23.3344 28.5234 24.5835 27.2743 24.5835 25.7335V13.6387C24.5835 12.0979 23.4365 11.1233 21.7937 10.8488Z" fill="currentColor"></path></svg>
					Docs</a>
			</li>
		<li><div class="relative ">
	<button class="px-2 py-0.5 group hover:text-green-700 dark:hover:text-gray-400 flex items-center " type="button">
		<svg class="mr-1.5 text-gray-400 group-hover:text-green-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M19 6H5a3 3 0 0 0-3 3v2.72L8.837 14h6.326L22 11.72V9a3 3 0 0 0-3-3z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M10 6V5h4v1h2V5a2.002 2.002 0 0 0-2-2h-4a2.002 2.002 0 0 0-2 2v1h2zm-1.163 8L2 11.72V18a3.003 3.003 0 0 0 3 3h14a3.003 3.003 0 0 0 3-3v-6.28L15.163 14H8.837z" fill="currentColor"></path></svg>
			Solutions
		</button>
	
	
	
	</div></li>
		<li><a class="group flex items-center px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-400" href="/pricing">Pricing
			</a></li>

		<li><div class="relative group">
	<button class="px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-600 flex items-center " type="button">
		<svg class="mr-1.5 text-gray-500 w-5 group-hover:text-gray-400 dark:text-gray-300 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 18" preserveAspectRatio="xMidYMid meet"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 3.30221C14.4504 2.836 14.8284 2.45807 15.2946 2.45807H28.4933C28.9595 2.45807 29.3374 2.836 29.3374 3.30221C29.3374 3.76842 28.9595 4.14635 28.4933 4.14635H15.2946C14.8284 4.14635 14.4504 3.76842 14.4504 3.30221Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 9.00002C14.4504 8.53382 14.8284 8.15588 15.2946 8.15588H28.4933C28.9595 8.15588 29.3374 8.53382 29.3374 9.00002C29.3374 9.46623 28.9595 9.84417 28.4933 9.84417H15.2946C14.8284 9.84417 14.4504 9.46623 14.4504 9.00002Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 14.6978C14.4504 14.2316 14.8284 13.8537 15.2946 13.8537H28.4933C28.9595 13.8537 29.3374 14.2316 29.3374 14.6978C29.3374 15.164 28.9595 15.542 28.4933 15.542H15.2946C14.8284 15.542 14.4504 15.164 14.4504 14.6978Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.94549 6.87377C2.27514 6.54411 2.80962 6.54411 3.13928 6.87377L6.23458 9.96907L9.32988 6.87377C9.65954 6.54411 10.194 6.54411 10.5237 6.87377C10.8533 7.20343 10.8533 7.73791 10.5237 8.06756L6.23458 12.3567L1.94549 8.06756C1.61583 7.73791 1.61583 7.20343 1.94549 6.87377Z" fill="currentColor"></path></svg>
			
		</button>
	
	
	
	</div></li>
		<li><hr class="h-5 w-0.5 border-none bg-gray-100 dark:bg-gray-800"></li>
		<li><a class="block cursor-pointer px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-400" href="/login">Log In
				</a></li>
			<li><a class="rounded-full border border-transparent bg-gray-900 px-3 py-1 leading-none text-white hover:border-black hover:bg-white hover:text-black" href="/join">Sign Up
					</a></li></ul></nav></div></header></div>
	
	<div class="SVELTE_HYDRATER contents" data-props="{}" data-target="GoogleAnalyticsTracker"></div>
	
	
	<div class="SVELTE_HYDRATER contents" data-props="{}" data-target="SSOBanner"></div>

	<main class="flex flex-1 flex-col"><div class="SVELTE_HYDRATER contents" data-props="{&quot;activeTab&quot;:&quot;files&quot;,&quot;author&quot;:{&quot;avatarUrl&quot;:&quot;https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/1608042047613-5f1158120c833276f61f1a84.jpeg?w=200&amp;h=200&amp;f=face&quot;,&quot;fullname&quot;:&quot;Niels Rogge&quot;,&quot;name&quot;:&quot;nielsr&quot;,&quot;type&quot;:&quot;user&quot;,&quot;isPro&quot;:false,&quot;isHf&quot;:true},&quot;canReadRepoSettings&quot;:false,&quot;dataset&quot;:{&quot;author&quot;:&quot;nielsr&quot;,&quot;cardExists&quot;:false,&quot;citation&quot;:&quot;@article{Jaume2019FUNSDAD,\n  title={FUNSD: A Dataset for Form Understanding in Noisy Scanned Documents},\n  author={Guillaume Jaume and H. K. Ekenel and J. Thiran},\n  journal={2019 International Conference on Document Analysis and Recognition Workshops (ICDARW)},\n  year={2019},\n  volume={2},\n  pages={1-6}\n}&quot;,&quot;description&quot;:&quot;https://guillaumejaume.github.io/FUNSD/&quot;,&quot;downloads&quot;:6921,&quot;downloadsAllTime&quot;:174533,&quot;id&quot;:&quot;nielsr/funsd&quot;,&quot;isLikedByUser&quot;:false,&quot;isWatchedByUser&quot;:false,&quot;lastModified&quot;:&quot;2021-07-27T07:59:20.000Z&quot;,&quot;likes&quot;:5,&quot;paperswithcode_id&quot;:&quot;&quot;,&quot;viewer&quot;:&quot;viewer&quot;,&quot;discussionsDisabled&quot;:false,&quot;repoType&quot;:&quot;dataset&quot;,&quot;private&quot;:false,&quot;gated&quot;:false,&quot;tags&quot;:[&quot;region:us&quot;],&quot;tag_objs&quot;:[{&quot;type&quot;:&quot;region&quot;,&quot;label&quot;:&quot;🇺🇸 Region: US&quot;,&quot;id&quot;:&quot;region:us&quot;}]},&quot;discussionsStats&quot;:{&quot;closed&quot;:1,&quot;open&quot;:4,&quot;total&quot;:5},&quot;isLoggedIn&quot;:false}" data-target="DatasetHeader"><header class="from-gray-50-to-white border-b border-gray-100 bg-gradient-to-t via-white dark:via-gray-950 pt-6 sm:pt-9"><div class="container relative "><h1 class="flex flex-wrap items-center leading-tight mb-3 text-lg md:text-xl"><a href="/datasets" class="group flex items-center"><svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
					<span class="mr-2.5 font-semibold text-gray-400 group-hover:text-gray-500">Datasets:</span></a>
			<div class="group flex flex-none items-center"><div class="relative mr-1.5 flex items-center">

			<img alt="" class="w-3.5 h-3.5 rounded-full " src="https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/1608042047613-5f1158120c833276f61f1a84.jpeg?w=200&amp;h=200&amp;f=face"></div>
		<a href="/nielsr" class="text-gray-400 hover:text-blue-600">nielsr</a>
		<div class="mx-0.5 text-gray-300">/</div></div>

<div class="max-w-full "><a class="break-words font-mono font-semibold hover:text-blue-600 " href="/datasets/nielsr/funsd">funsd</a>
	<button class="relative text-sm mr-4 inline-flex cursor-pointer items-center text-sm focus:outline-none  mx-0.5   text-gray-600 " title="Copy dataset name to clipboard" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	</button></div>
			<div class="inline-flex items-center overflow-hidden whitespace-nowrap rounded-md border bg-white text-sm leading-none text-gray-500  mr-2"><button class="relative flex items-center px-1.5 py-1 hover:bg-gradient-to-t focus:outline-none overflow-hidden from-red-50 to-transparent dark:from-red-900 dark:to-red-800"  title="Like"><svg class="left-1.5 absolute" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z"></path></svg>

		
		<span class="ml-4 pl-0.5">like</span></button>
	<button class="flex items-center border-l px-1.5 py-1 text-gray-400 hover:bg-gray-50 focus:bg-gray-100 focus:outline-none dark:hover:bg-gray-900 dark:focus:bg-gray-800" title="See users who liked this repository">5</button></div>

			</h1>
		<div class="mb-3 flex flex-wrap md:mb-4"></div>

		<div class="flex flex-col-reverse lg:flex-row lg:items-center lg:justify-between"><div class="-mb-px flex h-12 items-center overflow-x-auto overflow-y-hidden "><a class="tab-alternate " href="/datasets/nielsr/funsd"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
			Dataset card
			
			
		</a><a class="tab-alternate active" href="/datasets/nielsr/funsd/tree/main"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M21 19h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-8h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0 4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M9 19a1 1 0 0 1-1-1V6a1 1 0 0 1 2 0v12a1 1 0 0 1-1 1zm-6-4.333a1 1 0 0 1-.64-1.769L3.438 12l-1.078-.898a1 1 0 0 1 1.28-1.538l2 1.667a1 1 0 0 1 0 1.538l-2 1.667a.999.999 0 0 1-.64.231z" fill="currentColor"></path></svg>
			<span class="xl:hidden">Files</span>
				<span class="hidden xl:inline">Files and versions</span>
			
			
		</a><a class="tab-alternate " href="/datasets/nielsr/funsd/discussions"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M20.6081 3C21.7684 3 22.8053 3.49196 23.5284 4.38415C23.9756 4.93678 24.4428 5.82749 24.4808 7.16133C24.9674 7.01707 25.4353 6.93643 25.8725 6.93643C26.9833 6.93643 27.9865 7.37587 28.696 8.17411C29.6075 9.19872 30.0124 10.4579 29.8361 11.7177C29.7523 12.3177 29.5581 12.8555 29.2678 13.3534C29.8798 13.8646 30.3306 14.5763 30.5485 15.4322C30.719 16.1032 30.8939 17.5006 29.9808 18.9403C30.0389 19.0342 30.0934 19.1319 30.1442 19.2318C30.6932 20.3074 30.7283 21.5229 30.2439 22.6548C29.5093 24.3704 27.6841 25.7219 24.1397 27.1727C21.9347 28.0753 19.9174 28.6523 19.8994 28.6575C16.9842 29.4379 14.3477 29.8345 12.0653 29.8345C7.87017 29.8345 4.8668 28.508 3.13831 25.8921C0.356375 21.6797 0.754104 17.8269 4.35369 14.1131C6.34591 12.058 7.67023 9.02782 7.94613 8.36275C8.50224 6.39343 9.97271 4.20438 12.4172 4.20438H12.4179C12.6236 4.20438 12.8314 4.2214 13.0364 4.25468C14.107 4.42854 15.0428 5.06476 15.7115 6.02205C16.4331 5.09583 17.134 4.359 17.7682 3.94323C18.7242 3.31737 19.6794 3 20.6081 3ZM20.6081 5.95917C20.2427 5.95917 19.7963 6.1197 19.3039 6.44225C17.7754 7.44319 14.8258 12.6772 13.7458 14.7131C13.3839 15.3952 12.7655 15.6837 12.2086 15.6837C11.1036 15.6837 10.2408 14.5497 12.1076 13.1085C14.9146 10.9402 13.9299 7.39584 12.5898 7.1776C12.5311 7.16799 12.4731 7.16355 12.4172 7.16355C11.1989 7.16355 10.6615 9.33114 10.6615 9.33114C10.6615 9.33114 9.0863 13.4148 6.38031 16.206C3.67434 18.998 3.5346 21.2388 5.50675 24.2246C6.85185 26.2606 9.42666 26.8753 12.0653 26.8753C14.8021 26.8753 17.6077 26.2139 19.1799 25.793C19.2574 25.7723 28.8193 22.984 27.6081 20.6107C27.4046 20.212 27.0693 20.0522 26.6471 20.0522C24.9416 20.0522 21.8393 22.6726 20.5057 22.6726C20.2076 22.6726 19.9976 22.5416 19.9116 22.222C19.3433 20.1173 28.552 19.2325 27.7758 16.1839C27.639 15.6445 27.2677 15.4256 26.746 15.4263C24.4923 15.4263 19.4358 19.5181 18.3759 19.5181C18.2949 19.5181 18.2368 19.4937 18.2053 19.4419C17.6743 18.557 17.9653 17.9394 21.7082 15.6009C25.4511 13.2617 28.0783 11.8545 26.5841 10.1752C26.4121 9.98141 26.1684 9.8956 25.8725 9.8956C23.6001 9.89634 18.2311 14.9403 18.2311 14.9403C18.2311 14.9403 16.7821 16.496 15.9057 16.496C15.7043 16.496 15.533 16.4139 15.4169 16.2112C14.7956 15.1296 21.1879 10.1286 21.5484 8.06535C21.7928 6.66715 21.3771 5.95917 20.6081 5.95917Z" fill="#FF9D00"></path><path d="M5.50686 24.2246C3.53472 21.2387 3.67446 18.9979 6.38043 16.206C9.08641 13.4147 10.6615 9.33111 10.6615 9.33111C10.6615 9.33111 11.2499 6.95933 12.59 7.17757C13.93 7.39581 14.9139 10.9401 12.1069 13.1084C9.29997 15.276 12.6659 16.7489 13.7459 14.713C14.8258 12.6772 17.7747 7.44316 19.304 6.44221C20.8326 5.44128 21.9089 6.00204 21.5484 8.06532C21.188 10.1286 14.795 15.1295 15.4171 16.2118C16.0391 17.2934 18.2312 14.9402 18.2312 14.9402C18.2312 14.9402 25.0907 8.49588 26.5842 10.1752C28.0776 11.8545 25.4512 13.2616 21.7082 15.6008C17.9646 17.9393 17.6744 18.557 18.2054 19.4418C18.7372 20.3266 26.9998 13.1351 27.7759 16.1838C28.5513 19.2324 19.3434 20.1173 19.9117 22.2219C20.48 24.3274 26.3979 18.2382 27.6082 20.6107C28.8193 22.9839 19.2574 25.7722 19.18 25.7929C16.0914 26.62 8.24723 28.3726 5.50686 24.2246Z" fill="#FFD21E"></path></svg>
			Community
			<div class="ml-1.5 flex h-4 min-w-[1rem] items-center justify-center rounded px-1 text-xs leading-none shadow-sm bg-black text-white dark:bg-gray-800 dark:text-gray-200">5
				</div>
			
		</a>
	</div>
			</div></div></header></div>
	
<div class="container relative flex flex-col md:grid md:space-y-0 w-full md:grid-cols-12  space-y-4 md:gap-6 mb-16"><section class="pt-8 border-gray-100 col-span-full"><header class="flex flex-wrap items-center justify-start pb-2 md:justify-end lg:flex-nowrap"><div class="mr-4 flex min-w-0 basis-auto flex-wrap items-center md:flex-grow md:basis-full lg:basis-auto lg:flex-nowrap"><div class="SVELTE_HYDRATER contents" data-props="{&quot;path&quot;:&quot;funsd.py&quot;,&quot;repoName&quot;:&quot;nielsr/funsd&quot;,&quot;repoType&quot;:&quot;dataset&quot;,&quot;rev&quot;:&quot;main&quot;,&quot;refs&quot;:{&quot;branches&quot;:[{&quot;name&quot;:&quot;main&quot;,&quot;ref&quot;:&quot;refs/heads/main&quot;,&quot;targetCommit&quot;:&quot;cc411ada8b05f1f67d5348b3baeba45aa3218c1a&quot;}],&quot;tags&quot;:[],&quot;converts&quot;:[{&quot;name&quot;:&quot;parquet&quot;,&quot;ref&quot;:&quot;refs/convert/parquet&quot;,&quot;targetCommit&quot;:&quot;ec75f84e5eb8b46e31eeaf53089010c1d2e0546f&quot;}]},&quot;view&quot;:&quot;blob&quot;}" data-target="BranchSelector"><div class="relative mr-4 mb-2">
	<button class="text-sm md:text-base btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 text-gray-700 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M13 14c-3.36 0-4.46 1.35-4.82 2.24C9.25 16.7 10 17.76 10 19a3 3 0 0 1-3 3a3 3 0 0 1-3-3c0-1.31.83-2.42 2-2.83V7.83A2.99 2.99 0 0 1 4 5a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.31-.83 2.42-2 2.83v5.29c.88-.65 2.16-1.12 4-1.12c2.67 0 3.56-1.34 3.85-2.23A3.006 3.006 0 0 1 14 7a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.34-.88 2.5-2.09 2.86C17.65 11.29 16.68 14 13 14m-6 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1M7 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1m10 2a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1z" fill="currentColor"></path></svg>
			main
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M7 10l5 5l5-5z" fill="currentColor"></path></svg></button>
	
	
	
	</div></div>
		<div class="mb-2 flex items-center overflow-hidden"><a class="truncate text-gray-800 hover:underline" href="/datasets/nielsr/funsd/tree/main">funsd</a>
			<span class="mx-1 text-gray-300">/</span>
				<span class="dark:text-gray-300">funsd.py</span></div></div>

	
	</header>
			<div class="SVELTE_HYDRATER contents" data-props="{&quot;commitLast&quot;:{&quot;date&quot;:&quot;2021-07-27T07:59:20.000Z&quot;,&quot;subject&quot;:&quot;Update attribute names&quot;,&quot;authors&quot;:[{&quot;_id&quot;:&quot;5f1158120c833276f61f1a84&quot;,&quot;avatar&quot;:&quot;https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/1608042047613-5f1158120c833276f61f1a84.jpeg?w=200&amp;h=200&amp;f=face&quot;,&quot;isHf&quot;:true,&quot;user&quot;:&quot;nielsr&quot;}],&quot;commit&quot;:{&quot;id&quot;:&quot;cc411ada8b05f1f67d5348b3baeba45aa3218c1a&quot;,&quot;parentIds&quot;:[&quot;f515662179498ed802de0a25c97eda718ffce4f4&quot;]},&quot;title&quot;:&quot;Update attribute names&quot;},&quot;repo&quot;:{&quot;name&quot;:&quot;nielsr/funsd&quot;,&quot;type&quot;:&quot;dataset&quot;}}" data-target="LastCommit"><div class="from-gray-100-to-white flex items-baseline rounded-t-lg border border-b-0 bg-gradient-to-t px-3 py-2 dark:border-gray-800"><img class="mt-0.5 mr-2.5 h-4 w-4 self-center rounded-full" alt="nielsr's picture" src="https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/1608042047613-5f1158120c833276f61f1a84.jpeg?w=200&amp;h=200&amp;f=face">
			<div class="mr-5 flex flex-none items-center truncate"><a class="hover:underline" href="/nielsr">nielsr
					</a>
				<div class="mt-0.5 ml-1.5 rounded border border-yellow-200 bg-yellow-50 px-1 text-xs font-semibold uppercase text-yellow-500 dark:bg-yellow-800 dark:text-yellow-400" title="member of the Hugging Face team">HF staff
					</div>
			</div>
		<div class="mr-4 truncate font-mono text-sm text-gray-500 hover:prose-a:underline"><!-- HTML_TAG_START -->Update attribute names<!-- HTML_TAG_END --></div>
		<a class="rounded border bg-gray-50 px-1.5 text-sm hover:underline dark:border-gray-800 dark:bg-gray-900" href="/datasets/nielsr/funsd/commit/cc411ada8b05f1f67d5348b3baeba45aa3218c1a">cc411ad</a>
		
		<time class="ml-auto hidden flex-none truncate pl-2 text-gray-500 dark:text-gray-400 lg:block" datetime="2021-07-27T07:59:20" title="Tue, 27 Jul 2021 07:59:20 GMT">about 2 years ago</time></div></div>
			<div class="flex flex-wrap items-center border px-3 py-1.5 text-sm text-gray-800 dark:border-gray-800 dark:bg-gray-900">
				<a class="my-1 mr-4 flex items-center hover:underline " href="/datasets/nielsr/funsd/raw/main/funsd.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M31 16l-7 7l-1.41-1.41L28.17 16l-5.58-5.59L24 9l7 7z" fill="currentColor"></path><path d="M1 16l7-7l1.41 1.41L3.83 16l5.58 5.59L8 23l-7-7z" fill="currentColor"></path><path d="M12.419 25.484L17.639 6l1.932.518L14.35 26z" fill="currentColor"></path></svg>
							raw
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/datasets/nielsr/funsd/commits/main/funsd.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 4C9.383 4 4 9.383 4 16s5.383 12 12 12s12-5.383 12-12S22.617 4 16 4zm0 2c5.535 0 10 4.465 10 10s-4.465 10-10 10S6 21.535 6 16S10.465 6 16 6zm-1 2v9h7v-2h-5V8z" fill="currentColor"></path></svg>
							history
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/datasets/nielsr/funsd/blame/main/funsd.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12a12 12 0 0 1-12 12z" fill="currentColor"></path><path d="M11.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path><path d="M20.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path></svg>
							blame
						</a><a class="my-1 mr-4 flex items-center hover:underline text-green-600 dark:text-gray-300" href="/datasets/nielsr/funsd/edit/main/funsd.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M2 26h28v2H2z" fill="currentColor"></path><path d="M25.4 9c.8-.8.8-2 0-2.8l-3.6-3.6c-.8-.8-2-.8-2.8 0l-15 15V24h6.4l15-15zm-5-5L24 7.6l-3 3L17.4 7l3-3zM6 22v-3.6l10-10l3.6 3.6l-10 10H6z" fill="currentColor"></path></svg>
							contribute
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/datasets/nielsr/funsd/delete/main/funsd.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M12 12h2v12h-2z" fill="currentColor"></path><path d="M18 12h2v12h-2z" fill="currentColor"></path><path d="M4 6v2h2v20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8h2V6zm4 22V8h16v20z" fill="currentColor"></path><path d="M12 2h8v2h-8z" fill="currentColor"></path></svg>
							delete
						</a>
				<div class="mr-4 flex items-center text-gray-400"><svg class="text-gray-300 text-sm mr-1.5 -translate-y-px" width="1em" height="1em" viewBox="0 0 22 28" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.3634 10.3639C15.8486 10.8491 15.8486 11.6357 15.3634 12.1209L10.9292 16.5551C10.6058 16.8785 10.0814 16.8785 9.7579 16.5551L7.03051 13.8277C6.54532 13.3425 6.54532 12.5558 7.03051 12.0707C7.51569 11.5855 8.30234 11.5855 8.78752 12.0707L9.7579 13.041C10.0814 13.3645 10.6058 13.3645 10.9292 13.041L13.6064 10.3639C14.0916 9.8787 14.8782 9.8787 15.3634 10.3639Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M10.6666 27.12C4.93329 25.28 0 19.2267 0 12.7867V6.52001C0 5.40001 0.693334 4.41334 1.73333 4.01334L9.73333 1.01334C10.3333 0.786673 11 0.786673 11.6 1.02667L19.6 4.02667C20.1083 4.21658 20.5465 4.55701 20.8562 5.00252C21.1659 5.44803 21.3324 5.97742 21.3333 6.52001V12.7867C21.3333 19.24 16.4 25.28 10.6666 27.12Z" fill="currentColor" fill-opacity="0.22"></path><path d="M10.0845 1.94967L10.0867 1.94881C10.4587 1.8083 10.8666 1.81036 11.2286 1.95515L11.2387 1.95919L11.2489 1.963L19.2489 4.963L19.25 4.96342C19.5677 5.08211 19.8416 5.29488 20.0351 5.57333C20.2285 5.85151 20.3326 6.18203 20.3333 6.52082C20.3333 6.52113 20.3333 6.52144 20.3333 6.52176L20.3333 12.7867C20.3333 18.6535 15.8922 24.2319 10.6666 26.0652C5.44153 24.2316 1 18.6409 1 12.7867V6.52001C1 5.82357 1.42893 5.20343 2.08883 4.94803L10.0845 1.94967Z" stroke="currentColor" stroke-opacity="0.30" stroke-width="2"></path></svg>

							No virus
						</div>
				
				<div class="dark:text-gray-300 sm:ml-auto">4.54 kB</div></div>

			<div class="relative min-h-[100px] rounded-b-lg border border-t-0 leading-tight dark:border-gray-800 dark:bg-gray-925">
				<div class="py-3"><div class="SVELTE_HYDRATER contents" data-props="{&quot;lines&quot;:[&quot;<span class=\&quot;hljs-comment\&quot;># coding=utf-8</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> json&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> os&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> datasets&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> PIL <span class=\&quot;hljs-keyword\&quot;>import</span> Image&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> numpy <span class=\&quot;hljs-keyword\&quot;>as</span> np&quot;,&quot;&quot;,&quot;logger = datasets.logging.get_logger(__name__)&quot;,&quot;&quot;,&quot;&quot;,&quot;_CITATION = <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;\\</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>@article{Jaume2019FUNSDAD,</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>  title={FUNSD: A Dataset for Form Understanding in Noisy Scanned Documents},</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>  author={Guillaume Jaume and H. K. Ekenel and J. Thiran},</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>  journal={2019 International Conference on Document Analysis and Recognition Workshops (ICDARW)},</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>  year={2019},</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>  volume={2},</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>  pages={1-6}</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>}</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;_DESCRIPTION = <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;\\</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>https://guillaumejaume.github.io/FUNSD/</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>load_image</span>(<span class=\&quot;hljs-params\&quot;>image_path</span>):&quot;,&quot;    image = Image.<span class=\&quot;hljs-built_in\&quot;>open</span>(image_path).convert(<span class=\&quot;hljs-string\&quot;>&amp;quot;RGB&amp;quot;</span>)&quot;,&quot;    w, h = image.size&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> image, (w, h)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>normalize_bbox</span>(<span class=\&quot;hljs-params\&quot;>bbox, size</span>):&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> [&quot;,&quot;        <span class=\&quot;hljs-built_in\&quot;>int</span>(<span class=\&quot;hljs-number\&quot;>1000</span> * bbox[<span class=\&quot;hljs-number\&quot;>0</span>] / size[<span class=\&quot;hljs-number\&quot;>0</span>]),&quot;,&quot;        <span class=\&quot;hljs-built_in\&quot;>int</span>(<span class=\&quot;hljs-number\&quot;>1000</span> * bbox[<span class=\&quot;hljs-number\&quot;>1</span>] / size[<span class=\&quot;hljs-number\&quot;>1</span>]),&quot;,&quot;        <span class=\&quot;hljs-built_in\&quot;>int</span>(<span class=\&quot;hljs-number\&quot;>1000</span> * bbox[<span class=\&quot;hljs-number\&quot;>2</span>] / size[<span class=\&quot;hljs-number\&quot;>0</span>]),&quot;,&quot;        <span class=\&quot;hljs-built_in\&quot;>int</span>(<span class=\&quot;hljs-number\&quot;>1000</span> * bbox[<span class=\&quot;hljs-number\&quot;>3</span>] / size[<span class=\&quot;hljs-number\&quot;>1</span>]),&quot;,&quot;    ]&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>class</span> <span class=\&quot;hljs-title class_\&quot;>FunsdConfig</span>(datasets.BuilderConfig):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;BuilderConfig for FUNSD&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>__init__</span>(<span class=\&quot;hljs-params\&quot;>self, **kwargs</span>):&quot;,&quot;        <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;BuilderConfig for FUNSD.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;></span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        Args:</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>          **kwargs: keyword arguments forwarded to super.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;        <span class=\&quot;hljs-built_in\&quot;>super</span>(FunsdConfig, self).__init__(**kwargs)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>class</span> <span class=\&quot;hljs-title class_\&quot;>Funsd</span>(datasets.GeneratorBasedBuilder):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;FUNSD dataset.&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;&quot;,&quot;    BUILDER_CONFIGS = [&quot;,&quot;        FunsdConfig(name=<span class=\&quot;hljs-string\&quot;>&amp;quot;funsd&amp;quot;</span>, version=datasets.Version(<span class=\&quot;hljs-string\&quot;>&amp;quot;1.0.0&amp;quot;</span>), description=<span class=\&quot;hljs-string\&quot;>&amp;quot;FUNSD dataset&amp;quot;</span>),&quot;,&quot;    ]&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>_info</span>(<span class=\&quot;hljs-params\&quot;>self</span>):&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> datasets.DatasetInfo(&quot;,&quot;            description=_DESCRIPTION,&quot;,&quot;            features=datasets.Features(&quot;,&quot;                {&quot;,&quot;                    <span class=\&quot;hljs-string\&quot;>&amp;quot;id&amp;quot;</span>: datasets.Value(<span class=\&quot;hljs-string\&quot;>&amp;quot;string&amp;quot;</span>),&quot;,&quot;                    <span class=\&quot;hljs-string\&quot;>&amp;quot;words&amp;quot;</span>: datasets.<span class=\&quot;hljs-type\&quot;>Sequence</span>(datasets.Value(<span class=\&quot;hljs-string\&quot;>&amp;quot;string&amp;quot;</span>)),&quot;,&quot;                    <span class=\&quot;hljs-string\&quot;>&amp;quot;bboxes&amp;quot;</span>: datasets.<span class=\&quot;hljs-type\&quot;>Sequence</span>(datasets.<span class=\&quot;hljs-type\&quot;>Sequence</span>(datasets.Value(<span class=\&quot;hljs-string\&quot;>&amp;quot;int64&amp;quot;</span>))),&quot;,&quot;                    <span class=\&quot;hljs-string\&quot;>&amp;quot;ner_tags&amp;quot;</span>: datasets.<span class=\&quot;hljs-type\&quot;>Sequence</span>(&quot;,&quot;                        datasets.features.ClassLabel(&quot;,&quot;                            names=[<span class=\&quot;hljs-string\&quot;>&amp;quot;O&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;B-HEADER&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;I-HEADER&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;B-QUESTION&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;I-QUESTION&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;B-ANSWER&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;I-ANSWER&amp;quot;</span>]&quot;,&quot;                        )&quot;,&quot;                    ),&quot;,&quot;                    <span class=\&quot;hljs-string\&quot;>&amp;quot;image_path&amp;quot;</span>: datasets.Value(<span class=\&quot;hljs-string\&quot;>&amp;quot;string&amp;quot;</span>),&quot;,&quot;                }&quot;,&quot;            ),&quot;,&quot;            supervised_keys=<span class=\&quot;hljs-literal\&quot;>None</span>,&quot;,&quot;            homepage=<span class=\&quot;hljs-string\&quot;>&amp;quot;https://guillaumejaume.github.io/FUNSD/&amp;quot;</span>,&quot;,&quot;            citation=_CITATION,&quot;,&quot;        )&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>_split_generators</span>(<span class=\&quot;hljs-params\&quot;>self, dl_manager</span>):&quot;,&quot;        <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;Returns SplitGenerators.&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;        downloaded_file = dl_manager.download_and_extract(<span class=\&quot;hljs-string\&quot;>&amp;quot;https://guillaumejaume.github.io/FUNSD/dataset.zip&amp;quot;</span>)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> [&quot;,&quot;            datasets.SplitGenerator(&quot;,&quot;                name=datasets.Split.TRAIN, gen_kwargs={<span class=\&quot;hljs-string\&quot;>&amp;quot;filepath&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>f&amp;quot;<span class=\&quot;hljs-subst\&quot;>{downloaded_file}</span>/dataset/training_data/&amp;quot;</span>}&quot;,&quot;            ),&quot;,&quot;            datasets.SplitGenerator(&quot;,&quot;                name=datasets.Split.TEST, gen_kwargs={<span class=\&quot;hljs-string\&quot;>&amp;quot;filepath&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>f&amp;quot;<span class=\&quot;hljs-subst\&quot;>{downloaded_file}</span>/dataset/testing_data/&amp;quot;</span>}&quot;,&quot;            ),&quot;,&quot;        ]&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>_generate_examples</span>(<span class=\&quot;hljs-params\&quot;>self, filepath</span>):&quot;,&quot;        logger.info(<span class=\&quot;hljs-string\&quot;>&amp;quot;⏳ Generating examples from = %s&amp;quot;</span>, filepath)&quot;,&quot;        ann_dir = os.path.join(filepath, <span class=\&quot;hljs-string\&quot;>&amp;quot;annotations&amp;quot;</span>)&quot;,&quot;        img_dir = os.path.join(filepath, <span class=\&quot;hljs-string\&quot;>&amp;quot;images&amp;quot;</span>)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>for</span> guid, file <span class=\&quot;hljs-keyword\&quot;>in</span> <span class=\&quot;hljs-built_in\&quot;>enumerate</span>(<span class=\&quot;hljs-built_in\&quot;>sorted</span>(os.listdir(ann_dir))):&quot;,&quot;            words = []&quot;,&quot;            bboxes = []&quot;,&quot;            ner_tags = []&quot;,&quot;            file_path = os.path.join(ann_dir, file)&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>with</span> <span class=\&quot;hljs-built_in\&quot;>open</span>(file_path, <span class=\&quot;hljs-string\&quot;>&amp;quot;r&amp;quot;</span>, encoding=<span class=\&quot;hljs-string\&quot;>&amp;quot;utf8&amp;quot;</span>) <span class=\&quot;hljs-keyword\&quot;>as</span> f:&quot;,&quot;                data = json.load(f)&quot;,&quot;            image_path = os.path.join(img_dir, file)&quot;,&quot;            image_path = image_path.replace(<span class=\&quot;hljs-string\&quot;>&amp;quot;json&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;png&amp;quot;</span>)&quot;,&quot;            image, size = load_image(image_path)&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>for</span> item <span class=\&quot;hljs-keyword\&quot;>in</span> data[<span class=\&quot;hljs-string\&quot;>&amp;quot;form&amp;quot;</span>]:&quot;,&quot;                words_example, label = item[<span class=\&quot;hljs-string\&quot;>&amp;quot;words&amp;quot;</span>], item[<span class=\&quot;hljs-string\&quot;>&amp;quot;label&amp;quot;</span>]&quot;,&quot;                words_example = [w <span class=\&quot;hljs-keyword\&quot;>for</span> w <span class=\&quot;hljs-keyword\&quot;>in</span> words_example <span class=\&quot;hljs-keyword\&quot;>if</span> w[<span class=\&quot;hljs-string\&quot;>&amp;quot;text&amp;quot;</span>].strip() != <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;</span>]&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-built_in\&quot;>len</span>(words_example) == <span class=\&quot;hljs-number\&quot;>0</span>:&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>continue</span>&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> label == <span class=\&quot;hljs-string\&quot;>&amp;quot;other&amp;quot;</span>:&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>for</span> w <span class=\&quot;hljs-keyword\&quot;>in</span> words_example:&quot;,&quot;                        words.append(w[<span class=\&quot;hljs-string\&quot;>&amp;quot;text&amp;quot;</span>])&quot;,&quot;                        ner_tags.append(<span class=\&quot;hljs-string\&quot;>&amp;quot;O&amp;quot;</span>)&quot;,&quot;                        bboxes.append(normalize_bbox(w[<span class=\&quot;hljs-string\&quot;>&amp;quot;box&amp;quot;</span>], size))&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;                    words.append(words_example[<span class=\&quot;hljs-number\&quot;>0</span>][<span class=\&quot;hljs-string\&quot;>&amp;quot;text&amp;quot;</span>])&quot;,&quot;                    ner_tags.append(<span class=\&quot;hljs-string\&quot;>&amp;quot;B-&amp;quot;</span> + label.upper())&quot;,&quot;                    bboxes.append(normalize_bbox(words_example[<span class=\&quot;hljs-number\&quot;>0</span>][<span class=\&quot;hljs-string\&quot;>&amp;quot;box&amp;quot;</span>], size))&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>for</span> w <span class=\&quot;hljs-keyword\&quot;>in</span> words_example[<span class=\&quot;hljs-number\&quot;>1</span>:]:&quot;,&quot;                        words.append(w[<span class=\&quot;hljs-string\&quot;>&amp;quot;text&amp;quot;</span>])&quot;,&quot;                        ner_tags.append(<span class=\&quot;hljs-string\&quot;>&amp;quot;I-&amp;quot;</span> + label.upper())&quot;,&quot;                        bboxes.append(normalize_bbox(w[<span class=\&quot;hljs-string\&quot;>&amp;quot;box&amp;quot;</span>], size))&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>yield</span> guid, {<span class=\&quot;hljs-string\&quot;>&amp;quot;id&amp;quot;</span>: <span class=\&quot;hljs-built_in\&quot;>str</span>(guid), <span class=\&quot;hljs-string\&quot;>&amp;quot;words&amp;quot;</span>: words, <span class=\&quot;hljs-string\&quot;>&amp;quot;bboxes&amp;quot;</span>: bboxes, <span class=\&quot;hljs-string\&quot;>&amp;quot;ner_tags&amp;quot;</span>: ner_tags, <span class=\&quot;hljs-string\&quot;>&amp;quot;image_path&amp;quot;</span>: image_path}&quot;,&quot;&quot;],&quot;context&quot;:{&quot;repo&quot;:{&quot;name&quot;:&quot;nielsr/funsd&quot;,&quot;type&quot;:&quot;dataset&quot;},&quot;revision&quot;:&quot;cc411ada8b05f1f67d5348b3baeba45aa3218c1a&quot;,&quot;path&quot;:&quot;funsd.py&quot;}}" data-target="BlobContent">

<div class="relative text-sm"><div class="overflow-x-auto"><table class="min-w-full border-collapse font-mono"><tbody><tr class="" id="L1">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="1"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># coding=utf-8</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L2">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="2"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> json<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L3">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="3"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> os<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L4">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="4"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L5">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="5"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> datasets<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L6">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="6"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L7">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="7"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> PIL <span class="hljs-keyword">import</span> Image<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L8">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="8"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> numpy <span class="hljs-keyword">as</span> np<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L9">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="9"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L10">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="10"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->logger = datasets.logging.get_logger(__name__)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L11">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="11"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L12">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="12"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L13">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="13"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->_CITATION = <span class="hljs-string">&quot;&quot;&quot;\</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L14">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="14"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">@article{Jaume2019FUNSDAD,</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L15">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="15"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">  title={FUNSD: A Dataset for Form Understanding in Noisy Scanned Documents},</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L16">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="16"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">  author={Guillaume Jaume and H. K. Ekenel and J. Thiran},</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L17">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="17"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">  journal={2019 International Conference on Document Analysis and Recognition Workshops (ICDARW)},</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L18">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="18"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">  year={2019},</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L19">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="19"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">  volume={2},</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L20">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="20"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">  pages={1-6}</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L21">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="21"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">}</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L22">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="22"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L23">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="23"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->_DESCRIPTION = <span class="hljs-string">&quot;&quot;&quot;\</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L24">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="24"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">https://guillaumejaume.github.io/FUNSD/</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L25">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="25"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L26">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="26"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L27">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="27"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">load_image</span>(<span class="hljs-params">image_path</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L28">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="28"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    image = Image.<span class="hljs-built_in">open</span>(image_path).convert(<span class="hljs-string">&quot;RGB&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L29">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="29"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    w, h = image.size<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L30">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="30"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> image, (w, h)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L31">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="31"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L32">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="32"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">normalize_bbox</span>(<span class="hljs-params">bbox, size</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L33">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="33"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> [<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L34">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="34"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-built_in">int</span>(<span class="hljs-number">1000</span> * bbox[<span class="hljs-number">0</span>] / size[<span class="hljs-number">0</span>]),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L35">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="35"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-built_in">int</span>(<span class="hljs-number">1000</span> * bbox[<span class="hljs-number">1</span>] / size[<span class="hljs-number">1</span>]),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L36">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="36"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-built_in">int</span>(<span class="hljs-number">1000</span> * bbox[<span class="hljs-number">2</span>] / size[<span class="hljs-number">0</span>]),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L37">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="37"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-built_in">int</span>(<span class="hljs-number">1000</span> * bbox[<span class="hljs-number">3</span>] / size[<span class="hljs-number">1</span>]),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L38">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="38"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    ]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L39">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="39"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L40">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="40"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">class</span> <span class="hljs-title class_">FunsdConfig</span>(datasets.BuilderConfig):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L41">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="41"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;BuilderConfig for FUNSD&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L42">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="42"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L43">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="43"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">__init__</span>(<span class="hljs-params">self, **kwargs</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L44">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="44"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-string">&quot;&quot;&quot;BuilderConfig for FUNSD.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L45">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="45"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string"></span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L46">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="46"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        Args:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L47">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="47"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">          **kwargs: keyword arguments forwarded to super.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L48">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="48"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L49">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="49"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-built_in">super</span>(FunsdConfig, self).__init__(**kwargs)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L50">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="50"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L51">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="51"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">class</span> <span class="hljs-title class_">Funsd</span>(datasets.GeneratorBasedBuilder):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L52">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="52"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;FUNSD dataset.&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L53">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="53"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L54">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="54"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    BUILDER_CONFIGS = [<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L55">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="55"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        FunsdConfig(name=<span class="hljs-string">&quot;funsd&quot;</span>, version=datasets.Version(<span class="hljs-string">&quot;1.0.0&quot;</span>), description=<span class="hljs-string">&quot;FUNSD dataset&quot;</span>),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L56">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="56"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    ]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L57">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="57"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L58">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="58"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">_info</span>(<span class="hljs-params">self</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L59">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="59"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> datasets.DatasetInfo(<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L60">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="60"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            description=_DESCRIPTION,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L61">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="61"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            features=datasets.Features(<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L62">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="62"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                {<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L63">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="63"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    <span class="hljs-string">&quot;id&quot;</span>: datasets.Value(<span class="hljs-string">&quot;string&quot;</span>),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L64">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="64"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    <span class="hljs-string">&quot;words&quot;</span>: datasets.<span class="hljs-type">Sequence</span>(datasets.Value(<span class="hljs-string">&quot;string&quot;</span>)),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L65">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="65"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    <span class="hljs-string">&quot;bboxes&quot;</span>: datasets.<span class="hljs-type">Sequence</span>(datasets.<span class="hljs-type">Sequence</span>(datasets.Value(<span class="hljs-string">&quot;int64&quot;</span>))),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L66">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="66"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    <span class="hljs-string">&quot;ner_tags&quot;</span>: datasets.<span class="hljs-type">Sequence</span>(<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L67">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="67"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                        datasets.features.ClassLabel(<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L68">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="68"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                            names=[<span class="hljs-string">&quot;O&quot;</span>, <span class="hljs-string">&quot;B-HEADER&quot;</span>, <span class="hljs-string">&quot;I-HEADER&quot;</span>, <span class="hljs-string">&quot;B-QUESTION&quot;</span>, <span class="hljs-string">&quot;I-QUESTION&quot;</span>, <span class="hljs-string">&quot;B-ANSWER&quot;</span>, <span class="hljs-string">&quot;I-ANSWER&quot;</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L69">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="69"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                        )<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L70">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="70"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    ),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L71">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="71"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    <span class="hljs-string">&quot;image_path&quot;</span>: datasets.Value(<span class="hljs-string">&quot;string&quot;</span>),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L72">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="72"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                }<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L73">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="73"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            ),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L74">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="74"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            supervised_keys=<span class="hljs-literal">None</span>,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L75">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="75"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            homepage=<span class="hljs-string">&quot;https://guillaumejaume.github.io/FUNSD/&quot;</span>,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L76">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="76"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            citation=_CITATION,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L77">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="77"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L78">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="78"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L79">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="79"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">_split_generators</span>(<span class="hljs-params">self, dl_manager</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L80">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="80"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-string">&quot;&quot;&quot;Returns SplitGenerators.&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L81">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="81"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        downloaded_file = dl_manager.download_and_extract(<span class="hljs-string">&quot;https://guillaumejaume.github.io/FUNSD/dataset.zip&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L82">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="82"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> [<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L83">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="83"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            datasets.SplitGenerator(<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L84">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="84"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                name=datasets.Split.TRAIN, gen_kwargs={<span class="hljs-string">&quot;filepath&quot;</span>: <span class="hljs-string">f&quot;<span class="hljs-subst">{downloaded_file}</span>/dataset/training_data/&quot;</span>}<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L85">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="85"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            ),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L86">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="86"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            datasets.SplitGenerator(<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L87">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="87"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                name=datasets.Split.TEST, gen_kwargs={<span class="hljs-string">&quot;filepath&quot;</span>: <span class="hljs-string">f&quot;<span class="hljs-subst">{downloaded_file}</span>/dataset/testing_data/&quot;</span>}<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L88">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="88"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            ),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L89">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="89"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        ]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L90">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="90"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L91">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="91"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">_generate_examples</span>(<span class="hljs-params">self, filepath</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L92">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="92"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        logger.info(<span class="hljs-string">&quot;⏳ Generating examples from = %s&quot;</span>, filepath)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L93">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="93"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        ann_dir = os.path.join(filepath, <span class="hljs-string">&quot;annotations&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L94">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="94"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        img_dir = os.path.join(filepath, <span class="hljs-string">&quot;images&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L95">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="95"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">for</span> guid, file <span class="hljs-keyword">in</span> <span class="hljs-built_in">enumerate</span>(<span class="hljs-built_in">sorted</span>(os.listdir(ann_dir))):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L96">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="96"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            words = []<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L97">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="97"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            bboxes = []<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L98">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="98"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            ner_tags = []<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L99">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="99"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            file_path = os.path.join(ann_dir, file)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L100">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="100"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-keyword">with</span> <span class="hljs-built_in">open</span>(file_path, <span class="hljs-string">&quot;r&quot;</span>, encoding=<span class="hljs-string">&quot;utf8&quot;</span>) <span class="hljs-keyword">as</span> f:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L101">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="101"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                data = json.load(f)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L102">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="102"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            image_path = os.path.join(img_dir, file)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L103">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="103"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            image_path = image_path.replace(<span class="hljs-string">&quot;json&quot;</span>, <span class="hljs-string">&quot;png&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L104">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="104"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            image, size = load_image(image_path)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L105">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="105"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-keyword">for</span> item <span class="hljs-keyword">in</span> data[<span class="hljs-string">&quot;form&quot;</span>]:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L106">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="106"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                words_example, label = item[<span class="hljs-string">&quot;words&quot;</span>], item[<span class="hljs-string">&quot;label&quot;</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L107">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="107"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                words_example = [w <span class="hljs-keyword">for</span> w <span class="hljs-keyword">in</span> words_example <span class="hljs-keyword">if</span> w[<span class="hljs-string">&quot;text&quot;</span>].strip() != <span class="hljs-string">&quot;&quot;</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L108">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="108"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(words_example) == <span class="hljs-number">0</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L109">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="109"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">continue</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L110">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="110"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> label == <span class="hljs-string">&quot;other&quot;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L111">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="111"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">for</span> w <span class="hljs-keyword">in</span> words_example:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L112">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="112"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                        words.append(w[<span class="hljs-string">&quot;text&quot;</span>])<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L113">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="113"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                        ner_tags.append(<span class="hljs-string">&quot;O&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L114">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="114"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                        bboxes.append(normalize_bbox(w[<span class="hljs-string">&quot;box&quot;</span>], size))<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L115">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="115"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L116">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="116"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    words.append(words_example[<span class="hljs-number">0</span>][<span class="hljs-string">&quot;text&quot;</span>])<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L117">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="117"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    ner_tags.append(<span class="hljs-string">&quot;B-&quot;</span> + label.upper())<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L118">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="118"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    bboxes.append(normalize_bbox(words_example[<span class="hljs-number">0</span>][<span class="hljs-string">&quot;box&quot;</span>], size))<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L119">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="119"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">for</span> w <span class="hljs-keyword">in</span> words_example[<span class="hljs-number">1</span>:]:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L120">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="120"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                        words.append(w[<span class="hljs-string">&quot;text&quot;</span>])<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L121">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="121"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                        ner_tags.append(<span class="hljs-string">&quot;I-&quot;</span> + label.upper())<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L122">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="122"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                        bboxes.append(normalize_bbox(w[<span class="hljs-string">&quot;box&quot;</span>], size))<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L123">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="123"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-keyword">yield</span> guid, {<span class="hljs-string">&quot;id&quot;</span>: <span class="hljs-built_in">str</span>(guid), <span class="hljs-string">&quot;words&quot;</span>: words, <span class="hljs-string">&quot;bboxes&quot;</span>: bboxes, <span class="hljs-string">&quot;ner_tags&quot;</span>: ner_tags, <span class="hljs-string">&quot;image_path&quot;</span>: image_path}<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L124">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right text-gray-300 hover:text-black" data-line-num="124"></td>
						<td class="overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr></tbody></table></div>
	</div></div></div></div></section></div></main>
	</div>

		<script>
			import("/front/build/kube-72bd1c3/index.js");
			window.moonSha = "kube-72bd1c3/";
			window.hubConfig = JSON.parse(`{"features":{"signupDisabled":false,"awsMarketplace":false},"sshGitUrl":"git@hf.co","moonHttpUrl":"https://huggingface.co","captchaApiKey":"bd5f2066-93dc-4bdd-a64b-a24646ca3859","stripePublicKey":"pk_live_x2tdjFXBCvXo2FFmMybezpeM00J6gPCAAc","environment":"production","userAgent":"HuggingFace (production)"}`);
		</script>

		<!-- Stripe -->
		<script>
			if (["hf.co", "huggingface.co"].includes(window.location.hostname)) {
				const script = document.createElement("script");
				script.src = "https://js.stripe.com/v3/";
				script.async = true;
				document.head.appendChild(script);
			}
		</script>

		<!-- Google analytics v4 -->
		<script>
			if (["hf.co", "huggingface.co"].includes(window.location.hostname)) {
				const script = document.createElement("script");
				script.src = "https://www.googletagmanager.com/gtag/js?id=G-8Q63TH4CSL";
				script.async = true;
				document.head.appendChild(script);

				window.dataLayer = window.dataLayer || [];
				function gtag() {
					if (window.dataLayer !== undefined) {
						window.dataLayer.push(arguments);
					}
				}
				gtag("js", new Date());
				gtag("config", "G-8Q63TH4CSL", { page_path: "/datasets/nielsr/funsd/blob/main/funsd.py" });
				/// ^ See https://developers.google.com/analytics/devguides/collection/gtagjs/pages
				gtag("consent", "default", { ad_storage: "denied", analytics_storage: "denied" });
				/// ^ See https://developers.google.com/tag-platform/gtagjs/reference#consent
				/// TODO: ask the user for their consent and update this with gtag('consent', 'update')
			}
		</script>

		<!-- Google Analytics v3 (deprecated) -->
		<script>
			if (["hf.co", "huggingface.co"].includes(window.location.hostname)) {
				(function (i, s, o, g, r, a, m) {
					i["GoogleAnalyticsObject"] = r;
					(i[r] =
						i[r] ||
						function () {
							(i[r].q = i[r].q || []).push(arguments);
						}),
						(i[r].l = 1 * new Date());
					(a = s.createElement(o)), (m = s.getElementsByTagName(o)[0]);
					a.async = 1;
					a.src = g;
					m.parentNode.insertBefore(a, m);
				})(window, document, "script", "https://www.google-analytics.com/analytics.js", "ganalytics");
				ganalytics("create", "UA-83738774-2", "auto");
				ganalytics("send", "pageview", "/datasets/nielsr/funsd/blob/main/funsd.py");
			}
		</script>
	</body>
</html>
