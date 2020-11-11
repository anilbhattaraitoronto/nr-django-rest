<script>
    import { posts, newPosts, postTitles } from "../../stores/postStore.js";
</script>

<style>
</style>

<svelte:head>
    <title>Welcome | Nepal Reviewed</title>
</svelte:head>
<main class="section container p-0">
    <div class="hero has-background-success px-0 mx-0">
        <div class="hero-body ">
            <h1 class="title is-4 has-text-info-dark is-uppercase">
                Nepal Reviewed
            </h1>
            <h2 class="subtitle is-6 is-italic has-text-warning py-2">
                Simplifying academic works on Nepal
            </h2>
            <p class="py-2 has-text-grey-dark">
                We combine academic rigor and journalistic simplicity to produce
                knowledge for everyone so that everyone are better informed
                about the complex and dynamic reality in Nepal.
            </p>
            <p class="py-2 has-text-info">Welcome!</p>
        </div>
    </div>

    {#if $newPosts.length > 0}
        <article class="section container">
            <h2 class="title is-3">Latest</h2>
            <div class="container columns is-multiline  ">
                {#each $newPosts as post}
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
                                        class="pb-1 is-size-6 is-italic has-text-grey">
                                        {new Date(post.posted_date).toDateString()}
                                    </p>
                                    <h4
                                        class="is-italic is-size-5 has-text-black">
                                        <a
                                            href="#/categoryposts/{post.category}"
                                            class="has-text-black">{post.category}</a>
                                    </h4>
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
</main>
