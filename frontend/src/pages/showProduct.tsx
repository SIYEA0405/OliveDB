import Head from "next/head";
import Image from "next/image";
import styles from "@/styles/Home.module.css";
import ProductTable from "@/components/ProductTable";
import ProductChart from "@/components/ProductChart";
export default function showProduct() {
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
        <h1>결과창</h1>
        <ProductTable />
        <ProductChart
          data={[1, 2, 3, 4, 5]}
          labels={["One", "Two", "Three", "Four", "Five"]}
        />
      </main>
    </>
  );
}
