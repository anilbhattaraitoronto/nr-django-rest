<script>
    import { posts, topicPosts } from "../../stores/postStore.js";
    import { push, pop, replace } from "svelte-spa-router";
    import PostItem from "../shared/PostItem.svelte";
    export let params = {};

    // posts.subscribe(async (data) => {
    //     $topicPosts = await data.filter((post) =>
    //         post.topics.find((topic) => topic.slug == params.topic)
    //     );
    // });

    function getTopicPosts(slug) {
        posts.subscribe((data) => {
            $topicPosts = data.filter((post) =>
                post.topics.find((topic) => topic.slug == slug)
            );
        });
    }
    getTopicPosts(params.topic);
</script>

<svelte:head>
    <title>{params.topic} | Nepal Reviewed</title>
</svelte:head>

<h2 class="title">
    Posts on
    <span class="is-capitalized title is-2">{params.topic}</span>
</h2>
{#if $topicPosts.length > 0}
    <article class="section container px-0 pt-1">
        <div class="container columns is-multiline  ">
            {#each $topicPosts as post}
                <PostItem {post} />
            {/each}
        </div>
    </article>
{:else}
    <p>Posts on the way ...</p>
{/if}
