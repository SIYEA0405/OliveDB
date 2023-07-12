import Head from "next/head";
import Image from "next/image";
import styles from "@/styles/Home.module.css";
import SearchBar from "@/components/SearchBar";

export default function Home() {
  return (
    <>
      <Head>
        <title>OliveDB</title>
        <meta
          name="description"
          content="OliveDB is database of everything on Oliveyoung."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/oliveDB_logo.ico" />
      </Head>
      <main className={styles.main}>
        <SearchBar />
      </main>
    </>
  );
}
