import Head from "next/head";
import styles from "@/styles/Home.module.css";
import { useQuery } from "react-query";

interface ProductDataProps {
  _id: string;
  brand: string;
  large_ctg: string;
  name: string;
  price: {
    current: number;
    lowest: number;
    original: number;
  };
  small_ctg: string[];
}

interface ShowProductListProps {
  products: ProductDataProps[];
}

const ShowProductList: React.FC<ShowProductListProps> = ({ products }) => {
  return (
    <>
      <main className={styles.main}>
        <h1>{}로 검색한 결과는 총 0개 입니다.</h1>
      </main>
    </>
  );
};

export default ShowProductList;
