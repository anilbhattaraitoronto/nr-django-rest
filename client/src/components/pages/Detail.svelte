<script>
    import { posts, postDetail } from "../../stores/postStore.js";
    import { push, pop, replace } from "svelte-spa-router";
    export let params = {};

    posts.subscribe((data) => {
        $postDetail = data.find((item) => item.id == params.id);
    });
</script>

<svelte:head>
    {#if $postDetail}
        <title>{$postDetail.title} | Nepal Reviewed</title>
    {/if}
</svelte:head>
{#if $postDetail}
    <div class="post container card p-4 ">
        {#if $postDetail.imageurl}
            <div class="card-image">
                <figure class="image is-4by3">
                    <img src={$postDetail.imageurl} alt="" />
                </figure>
            </div>
        {:else if $postDetail.image}
            <div class="card-image">
                <figure class="image is-4by3">
                    <img src={$postDetail.image} alt="" />
                </figure>
            </div>
        {/if}
        <h3 class="has-text-black">
            <a
                href="#/categoryposts/{$postDetail.category}"
                class="has-text-black is-capitalized">{$postDetail.category}</a>
        </h3>
        <h2 class="title">{$postDetail.title}</h2>
        <h2 class="has-text-black">{$postDetail.author}</h2>
        {@html $postDetail.content}
        <p>
            Topics:
            {#each $postDetail.topics as topic}
                <a
                    href="#/topicposts/{topic.name}"
                    class="button">{topic.name}</a>
            {/each}
        </p>
    </div>
{/if}
