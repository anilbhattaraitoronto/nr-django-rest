<script>
    import { posts, postTitles, topicPosts } from "../../stores/postStore.js";
    import { push, pop, replace } from "svelte-spa-router";

    export let params = {};

    posts.subscribe(async (data) => {
        $topicPosts = await data.filter((post) =>
            post.topics.find((topic) => topic.slug == params.topic)
        );
    });
</script>

<svelte:head>
    <title>{params.topic} | Nepal Reviewed</title>
</svelte:head>

<h2 class="title">
    Posts on
    <span class="is-capitalized title is-2">{params.topic}</span>
</h2>
{#if $topicPosts.length > 0}
    <div class="container columns m-0">
        {#each $topicPosts as post}
            <div class="column is-half mb-2">
                <div class="card">
                    {#if post.imageurl}
                        <div class="card-image">
                            <figure class="image is-4by3">
                                <img src={post.imageurl} alt="" />
                            </figure>
                        </div>
                    {:else if post.thumbnail}
                        <div class="card-image">
                            <figure class="image is-4by3">
                                <img src={post.thumbnail} alt="" />
                            </figure>
                        </div>
                    {/if}
                    <div class="post card-content">
                        <h4 class="is-italic is-size-5 has-text-black">
                            <a
                                href="#/categoryposts/{post.category}"
                                class="has-text-black">{post.category}</a>
                        </h4>
                        <h3 class="title">
                            <a
                                href="#/{post.id}/{post.category}/{post.slug}"
                                class="has-text-weight-bold is-link is-size-3">{post.title}</a>
                        </h3>
                        <h4 class="has-text-weight-bold has-text-black">
                            {post.author}
                        </h4>
                        <p>
                            <span
                                class="button is-small is-link is-outlined">Topics:
                            </span>

                            {#each post.topics as topic}
                                <a
                                    href="#/topicposts/{topic.name}"
                                    class="button">{topic.name}</a>
                            {/each}
                        </p>
                        <p class="card-content has-text-right">
                            <a
                                href="#/{post.id}/{post.category}/{post.slug}"
                                class="has-text-weight-bold is-link">Read full
                                article</a>
                        </p>
                    </div>
                </div>
            </div>
        {/each}
    </div>
{:else}
    <p>Posts on the way ...</p>
{/if}
