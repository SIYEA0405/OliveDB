import { Box } from "@chakra-ui/react";
import {
  useReactTable,
  createColumnHelper,
  flexRender,
  getCoreRowModel,
  getSortedRowModel,
} from "@tanstack/react-table";
import { ProductDataProps } from "../../types";
import { numberWithCommas } from "../../utils/numberUtils";

interface ProductTableProps {
  data: ProductDataProps[];
}

const columnHelper = createColumnHelper<ProductDataProps>();

const columns = [
  columnHelper.accessor("_id", {
    header: "id",
    cell: (info) => info.getValue(),
  }),
  columnHelper.accessor("name", {
    header: "상품명",
    cell: (info) => info.getValue(),
  }),
  columnHelper.accessor("brand", {
    header: "브랜드",
    cell: (info) => info.getValue(),
  }),
  columnHelper.accessor("price.original", {
    header: "정가",
    cell: (info) => numberWithCommas(info.getValue()),
  }),
  columnHelper.accessor("price.current", {
    header: "현재가",
    cell: (info) => numberWithCommas(info.getValue()),
  }),
  columnHelper.accessor("price.lowest", {
    header: "최저가",
    cell: (info) => numberWithCommas(info.getValue()),
  }),
];

export default function ProductTable({ data }: ProductTableProps) {
  const tableInstance = useReactTable({
    columns,
    data,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
  });
  return (
    <>
      <Box borderWidth="1px" borderRadius="md">
        <table>
          <thead>
            {tableInstance.getHeaderGroups().map((headerGroup) => (
              <tr key={headerGroup.id}>
                {headerGroup.headers.map((header) => (
                  <th key={header.id}>
                    {header.isPlaceholder
                      ? null
                      : flexRender(
                          header.column.columnDef.header,
                          header.getContext()
                        )}
                  </th>
                ))}
              </tr>
            ))}
          </thead>
          <tbody>
            {tableInstance.getRowModel().rows.map((row) => (
              <tr key={row.id}>
                {row.getVisibleCells().map((cell) => (
                  <td key={cell.id}>
                    {flexRender(
                      cell.column.columnDef.cell,
                      cell.getContext()
                    )}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </Box>
    </>
  );
}
