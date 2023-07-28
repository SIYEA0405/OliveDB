import Head from "next/head";
import styles from "@/styles/Home.module.css";
import ProductTable from "@/components/ProductTable";
import ProductChart from "@/components/ProductChart";
export default function showProduct() {
  return (
    <>
      <main className={styles.main}>
        <h1>결과창</h1>
        {/* <ProductTable /> */}
        <ProductChart
          data={[1, 2, 3, 4, 5]}
          labels={["One", "Two", "Three", "Four", "Five"]}
        />
      </main>
    </>
  );
}
