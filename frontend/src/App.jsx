import './App.css'

function App() {
  return (
    <main className="app">
      <section className="hero">
        <p className="year-tag">Arcade Game of the Year — 1985</p>
        <h1>Gauntlet</h1>
        <p className="subtitle">
          Atari&apos;s dungeon crawler blended co-op action, nonstop enemy waves,
          and iconic narration into one of the most influential arcade experiences ever made.
        </p>
      </section>

      <section className="info-grid" aria-label="Gauntlet highlights">
        <article className="card">
          <h2>Why it stood out</h2>
          <p>
            Four-player simultaneous gameplay felt revolutionary in arcades and made
            every run feel like a team adventure.
          </p>
        </article>

        <article className="card">
          <h2>Signature moment</h2>
          <p>
            The booming voice line, &quot;Wizard needs food badly,&quot; became a defining
            phrase of 1980s gaming culture.
          </p>
        </article>

        <article className="card">
          <h2>Legacy</h2>
          <p>
            Gauntlet helped shape multiplayer action games and inspired generations
            of co-op dungeon crawlers across console and PC.
          </p>
        </article>
      </section>
    </main>
  )
}

export default App
