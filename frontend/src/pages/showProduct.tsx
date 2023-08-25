import Head from "next/head";
import styles from "@/styles/Home.module.css";
import ProductTable from "@/components/ProductTable";
export default function showProduct() {
  return (
    <>
      <main className={styles.main}>
        <h1>결과창</h1>
        {/* <ProductTable /> */}
      </main>
    </>
  );
}
