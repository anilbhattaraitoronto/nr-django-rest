<script>
    import { posts, categoryPosts } from "../../stores/postStore.js";
    import { push, pop, replace } from "svelte-spa-router";
    export let params = {};

    posts.subscribe(async (data) => {
        console.log("data is", data);
        $categoryPosts = await data.filter(
            (item) => item.category === params.category
        );
    });
</script>

<svelte:head>
    <title>{params.category} | Nepal Reviewed</title>
</svelte:head>
<h2 class="title is-capitalized">{params.category}</h2>
{#if $categoryPosts.length > 0}
    <article class="section container px-0 pt-1">
        <div class="container columns is-multiline  ">
            {#each $categoryPosts as post}
                <div class=" column is-half">
                    <div class="m-1">
                        <div class="card p-0 m-0">
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
                                <p
                                    class="pb-1 is-size-7 is-italic has-text-grey">
                                    {new Date(post.posted_date).toDateString()}
                                    /
                                    <a
                                        href="#/categoryposts/{post.category}"
                                        class="has-text-black">#{post.category}</a>
                                </p>

                                <h3 class="title">
                                    <a
                                        href="#/{post.id}/{post.category}/{post.slug}"
                                        class="has-text-weight-bold has-text-dark is-size-3">{post.title}</a>
                                </h3>
                                <h4
                                    class="has-text-weight-bold has-text-black pb-4">
                                    {post.author}
                                </h4>

                                <p class="has-text-grey is-italic">
                                    {post.summary.substring(0, 50)}
                                    ...
                                    <a
                                        href="#/{post.id}/{post.category}/{post.slug}"
                                        class="has-text-weight-bold is-link">Read
                                        full article</a>
                                </p>

                                <p>
                                    <span
                                        class="button is-small is-warning">Topics:
                                    </span>

                                    {#each post.topics as topic}
                                        <a
                                            href="#/topicposts/{topic.name}"
                                            class="">{topic.name}
                                            |
                                        </a>
                                    {/each}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- End of post column -->
            {/each}
        </div>
    </article>
{:else}
    <p>Posts on the way ...</p>
{/if}
