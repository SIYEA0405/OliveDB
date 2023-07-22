import Head from "next/head";
import styles from "@/styles/Home.module.css";
export default function showProductList() {
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
        <h1>{}로 검색한 결과는 총 0개 입니다.</h1>
      </main>
    </>
  );
}
