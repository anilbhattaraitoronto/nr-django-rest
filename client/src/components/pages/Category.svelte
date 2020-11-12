<script>
    import { posts, categoryPosts } from "../../stores/postStore.js";
    import { push, pop, replace } from "svelte-spa-router";
    import PostItem from "../shared/PostItem.svelte";
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
                <PostItem {post} />
            {/each}
        </div>
    </article>
{:else}
    <p>Posts on the way ...</p>
{/if}
