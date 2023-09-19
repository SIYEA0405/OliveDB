import type { NextApiRequest, NextApiResponse } from "next";
import axios from "axios";
import { ProductDataProps } from "../../../types";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<ProductDataProps[] | { message: string }>
) {
  const { search } = req.query;
  const apiUrl = process.env.NEXT_PUBLIC_API_KEY as string;
  try {
    const response = await axios.get(`${apiUrl}/products`, {
      params: {
        search: search,
      },
    });
    res.status(200).json(response.data);
  } catch (error: unknown) {
    if (error instanceof Error) {
      res.status(500).json({
        message: error.message,
      });
    } else {
      res.status(500).json({
        message: "An unexpected error occurred.",
      });
    }
  }
}
