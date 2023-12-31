export interface ProductDataProps {
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

interface DatesProps {
  date: string;
  price: number;
}

export interface PriceByDateDataProps {
  _id: string;
  dates: DatesProps[];
}
