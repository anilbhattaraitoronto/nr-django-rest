<script>
    import { onMount } from "svelte";
    import {
        posts,
        postTitles,
        newPosts,
        featuredPosts,
        categoryPosts,
        topicPosts,
        postDetail,
    } from "./stores/postStore.js";

    import Router from "svelte-spa-router";
    import { wrap } from "svelte-spa-router/wrap";

    import Home from "./components/pages/Home.svelte";
    import About from "./components/pages/About.svelte";
    import Category from "./components/pages/Category.svelte";
    import Detail from "./components/pages/Detail.svelte";
    import Topic from "./components/pages/Topic.svelte";

    //categories
    const categories = [
        {
            name: "Article Reviews",
            slug: "article-reviews",
        },
        {
            name: "Book Reviews",
            slug: "book-reviews",
        },
        {
            name: "Commentaries",
            slug: "commentaries",
        },
    ];
    const topics = [
        {
            name: "Air",
            slug: "air",
        },
        {
            name: "Water",
            slug: "water",
        },
        {
            name: "Food",
            slug: "food",
        },
        {
            name: "Housing",
            slug: "housing",
        },
        {
            name: "Health",
            slug: "health",
        },
        {
            name: "Education",
            slug: "education",
        },
        {
            name: "Transportation",
            slug: "transportation",
        },
        {
            name: "Sexuality",
            slug: "sexuality",
        },
    ];

    onMount(() => {
        fetch("posts/api/posts/")
            .then((response) => response.json())
            .then((data) => {
                if (data.length > 0) {
                    $posts = data;
                    $newPosts = data.filter((item) => item.is_new === true);
                    $featuredPosts = data.filter(
                        (item) => item.featured === true
                    );
                } else {
                    $posts = [];
                }
            })
            .catch((err) => console.log("Error: ", err));
    });

    const routes = {
        "/": Home,
        "/about": About,
        "/categoryposts/:category": Category,
        "/topicposts/:topic": Topic,
        "/:id/:category/:slug": Detail,
    };

    //get category Posts

    function getCategoryPosts(slug) {
        posts.subscribe((data) => {
            $categoryPosts = data.filter((item) => item.category === slug);
            console.log($categoryPosts);
        });
        toggleNavbar();
    }
    function getTopicPosts(slug) {
        posts.subscribe((data) => {
            $topicPosts = data.filter((post) =>
                post.topics.find((topic) => topic.slug == slug)
            );
        });
        toggleNavbar();
    }

    function getPostDetail(id) {
        posts.subscribe((data) => {
            $postDetail = data.find((post) => post.id == id);
        });
    }

    //toggle navbar

    let is_active = false;

    function toggleNavbar() {
        is_active == false ? (is_active = true) : (is_active = false);
    }
</script>

<main class=" section container p-0 ">
    <nav class=" navbar is-success px-3 is-fixed-top">
        <div class="navbar-brand">
            <a href="#/" class="navbar-item">Home</a>
            <a href="#/about" class="navbar-item">About</a>
            <span
                class="navbar-burger burger {is_active == true ? 'is-active' : ''}"
                on:click={toggleNavbar}>
                <span />
                <span />
                <span />
            </span>
        </div>
        <div class="navbar-menu {is_active == true ? 'is-active' : ''} ">
            <div class="navbar-end">
                <div class="navbar-item has-dropdown is-hoverable px-0">
                    <span class="navbar-link">Categories</span>
                    <div class="navbar-dropdown p-0">
                        {#each categories as category}
                            <a
                                href="#/categoryposts/{category.slug}"
                                on:click={() => getCategoryPosts(category.slug)}
                                class="navbar-item p-0 button is-success mt-1 has-text-centered">{category.name}</a>
                        {/each}
                    </div>
                </div>
                <div class="navbar-item has-dropdown is-hoverable px-0 mr-0">
                    <span class="navbar-link pr-6 ">Topics</span>
                    <div class="navbar-dropdown p-0">
                        {#each topics as topic}
                            <a
                                href="#/topicposts/{topic.slug}"
                                on:click={() => getTopicPosts(topic.slug)}
                                class="navbar-item p-0 button is-success mt-1 has-text-centered">{topic.name}</a>
                        {/each}
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <div class="container columns px-0 m-0 mt-2">
        <div class="column is-three-quarters p-0">
            <Router {routes} />
        </div>
        <div class="column mx-1 has-background-success-light">
            <h2 class="title">Recent</h2>
            <div class="p-0 ">
                {#each $postTitles as item}
                    <a
                        href="#/{item.id}/{item.category}/{item.slug}"
                        on:click={() => getPostDetail(item.id)}
                        class=" has-text-link">{item.title}</a>

                    <hr
                        style="margin:8px auto; "
                        class="has-background-white" />
                {/each}
            </div>
        </div>
    </div>
</main>
