<script>
    import { fade } from "svelte/transition";
    import { categories, topics } from "../../App.svelte";
</script>

<svelte:head>
    <title>About | Nepal Reviewed</title>
</svelte:head>
<div class="hero">
    <div class="hero-body">
        <h2 class="title is-3">About NR</h2>
        <main class="media p-2">
            <figure class="media-left">
                <p class="image is-64x64">
                    <img src="/static/np_flag.png" alt="" />
                </p>
            </figure>
            <div class="media-content">
                <p>
                    <strong>Nepal Reviewed</strong>
                    aims to make available academic works on Nepal in forms
                    accessible to ordinary Nepali readers. Access to academic
                    resources is an important part of deepening our
                    understanding about the complex and perennially changing
                    reality.
                </p>
                <p>
                    Academics are the keepers of modern society's conscience.
                    They are the only ones who could spend a long time
                    understanding the reality deeply. They are trained in
                    methods that allow for deeper understanding. One problem
                    with their works is, most of the time, these works are not
                    prepared for ordinary citizens. They are meant for debates
                    within the own community of relevant scholars. Academics
                    write in academic journals or present their ideas to their
                    peers in conferences.
                </p>
                <p>
                    Their works are not always limited to their peers as many of
                    them also translate them into products. This is particularly
                    true for various scientific fields with practical focus.
                </p>
                <p>
                    Social scientists, however, have lagged in 'translating'
                    their works.
                    <strong>Nepal Reviewed </strong>aims to do that in its own
                    modest way in relation to the academic works on Nepal.
                </p>
                <p>
                    <strong>NR</strong>
                    'translates' academic works on the following eight topics
                    into publicly accessible forms. It does so not by literal
                    translation but through snippets of topical writings that
                    are based on academic works.
                </p>
                <ul class="p-2 has-background-success-light">
                    <h3 class="title is-4">Topics</h3>
                    {#each topics as topic}
                        <li>
                            <a href="#/topicposts/{topic.slug}">{topic.name}</a>
                        </li>
                    {/each}
                </ul>

                <ul class="p-2 my-3 has-background-success-light">
                    <h3 class="title is-4">Three Forms</h3>
                    <p>NR produces three forms of writings:</p>
                    {#each categories as category}
                        <li>
                            <a
                                href="#/categoryposts/{category.slug}">{category.name}</a>
                        </li>
                    {/each}
                </ul>
                <p>
                    As the names suggest, the first two are reviews of academic
                    articles and books. The commentaries are slightly longer
                    form of writings in journalistic simplicity but written with
                    academic rigor.
                </p>
                <p>
                    Each review (article, or book) is based on a single article.
                    Commentaries can be based on more than one academic works or
                    can be entirely based on available data or can also be based
                    on only scholarly observations and arguments.
                </p>
            </div>
        </main>
    </div>
</div>
